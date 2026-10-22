"""Minimal participant interface: a standard-library HTTP server.

Flow per round: read the explanation -> watch rollouts A and B -> pick the one
that matches the explained policy -> rate the explanation and optionally say
what to change -> next round. The explanation is hidden during the test by
default (``ui.show_explanation_during_test``), so the test measures what the
participant took away rather than text matching. Correctness is not shown by
default (``ui.reveal_correctness``) so it cannot bias the rating.

Run with ``python experiments/explanations/serve_study.py --config ...``.
"""

from __future__ import annotations

import html
import re
import threading
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from typing import Any
from urllib.parse import parse_qs, quote, urlparse

from robocode.explanations.feedback import (
    RATING_QUESTION,
    TEXT_QUESTION,
    collect_feedback,
)
from robocode.explanations.runner import StudySession
from robocode.explanations.study import StudyContext, assign_condition

STYLE = """
body { font-family: system-ui, sans-serif; max-width: 1100px; margin: 2em auto; padding: 0 16px;
       line-height: 1.5; color: #1d1d1f; background: #fff; }
.explanation { max-width: 760px; border: 1px solid #ddd; border-radius: 8px; padding: 1em 1.5em; }
.videos { display: flex; gap: 24px; flex-wrap: wrap; }
.videos figure { margin: 0; flex: 1 1 400px; }
.videos img { width: 100%; border: 1px solid #ccc; border-radius: 6px; }
button { font-size: 1em; padding: .5em 1.4em; margin-top: 1em; }
.muted { color: #666; font-size: .9em; }
code { background: #f3f3f3; padding: 0 .25em; border-radius: 3px; }
"""


def render_markdown(text: str) -> str:
    """A small, safe Markdown subset: headings, lists, bold, inline code, paragraphs."""

    def inline(s: str) -> str:
        s = html.escape(s)
        s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
        s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
        return re.sub(r"(?<![*\w])\*([^*]+)\*(?!\w)", r"<em>\1</em>", s)

    out: list[str] = []
    in_list: str | None = None
    in_code = False
    for line in text.splitlines():
        if line.strip().startswith("```"):
            if in_list:
                out.append(f"</{in_list}>")
                in_list = None
            out.append("</pre>" if in_code else "<pre>")
            in_code = not in_code
            continue
        if in_code:
            out.append(html.escape(line))
            continue
        bullet = re.match(r"^\s*[-*+]\s+(.*)", line)
        number = re.match(r"^\s*\d+\.\s+(.*)", line)
        kind = "ul" if bullet else "ol" if number else None
        if in_list and kind != in_list:
            out.append(f"</{in_list}>")
            in_list = None
        if kind:
            if not in_list:
                out.append(f"<{kind}>")
                in_list = kind
            match = bullet or number
            assert match is not None
            out.append(f"<li>{inline(match.group(1))}</li>")
            continue
        heading = re.match(r"^(#{1,6})\s+(.*)", line)
        if heading:
            level = min(6, len(heading.group(1)) + 1)
            out.append(f"<h{level}>{inline(heading.group(2))}</h{level}>")
        elif line.strip():
            out.append(f"<p>{inline(line)}</p>")
    if in_list:
        out.append(f"</{in_list}>")
    if in_code:
        out.append("</pre>")
    return "\n".join(out)


def _page(title: str, body: str) -> bytes:
    return (
        f"<!doctype html><html><head><meta charset='utf-8'>"
        f"<meta name='viewport' content='width=device-width, initial-scale=1'>"
        f"<title>{html.escape(title)}</title><style>{STYLE}</style></head>"
        f"<body>{body}</body></html>"
    ).encode()


_DISABLE_ON_SUBMIT = (
    "var b=this.querySelector('button');b.disabled=true;b.textContent='Please wait...'"
)
# POST action -> the step the participant must be on for it to apply.
ACTION_STEP = {"to_test": "explanation", "answer": "test", "feedback": "feedback"}


def _form(user_id: str, action: str, round_index: int) -> str:
    """Opening tag of a step form, tagged with its round to detect stale posts."""
    return (
        f"<form method='post' action='/u/{quote(user_id)}/{action}' "
        f'onsubmit="{_DISABLE_ON_SUBMIT}">'
        f"<input type='hidden' name='round' value='{round_index}'>"
    )


class StudyApp:
    """Holds sessions and renders each step of a round."""

    def __init__(self, ctx: StudyContext) -> None:
        self.ctx = ctx
        ui = ctx.cfg.get("ui", {})
        self.show_explanation_during_test = bool(
            ui.get("show_explanation_during_test", False)
        )
        self.reveal_correctness = bool(ui.get("reveal_correctness", False))
        self.conditions = list(ctx.cfg.conditions)
        self.sessions: dict[str, StudySession] = {}
        self.locks: dict[str, threading.Lock] = {}
        self._registry_lock = threading.Lock()

    def session(self, user_id: str) -> StudySession:
        """The live session for ``user_id``; raises KeyError if not started."""
        return self.sessions[user_id]

    def start(self, user_id: str, condition: str | None) -> StudySession:
        """Start or resume a session.

        Condition defaults to hashed assignment.
        """
        with self._registry_lock:
            if user_id in self.sessions:
                return self.sessions[user_id]
            condition = condition or assign_condition(
                int(self.ctx.cfg.study_seed), user_id, self.conditions
            )
            if condition not in self.conditions:
                raise ValueError(f"Unknown condition {condition!r}")
            session = self.ctx.make_session(user_id, condition, {"simulated": False})
            self.sessions[user_id] = session
            self.locks[user_id] = threading.Lock()
            return session

    @staticmethod
    def current_step(session: StudySession) -> str:
        """The page this participant should be on, from the session state."""
        if session.done:
            return "done"
        state = session.current
        if state is None or state.test_shown_at is None:
            return "explanation"
        if state.answer is None:
            return "test"
        return "feedback"

    # ------------------------------------------------------------------ pages

    def start_page(self) -> bytes:
        """User id and (researcher-selected) condition."""
        options = "".join(f"<option value='{c}'>{c}</option>" for c in self.conditions)
        return _page(
            "Policy explanation study",
            "<h1>Policy explanation study</h1>"
            "<p>Each round you will read an explanation of a robot policy, then watch "
            "two "
            "short videos and pick the one that shows the explained policy. Both "
            "videos may "
            "complete the task; what differs is <em>how</em>. Then you will rate the "
            "explanation.</p>"
            "<form method='post' action='/start'>"
            "<p><label>Participant ID <input name='user_id' required "
            "pattern='[A-Za-z0-9_.-]+'></label></p>"
            "<p><label>Condition <select name='condition'><option value=''>assign "
            "automatically</option>"
            f"{options}</select></label> <span class='muted'>(set by the "
            "researcher)</span></p>"
            "<button>Start</button></form>",
        )

    def explanation_page(self, user_id: str) -> bytes:
        """Generate (once) and show this round's explanation."""
        session = self.session(user_id)
        if session.done:
            return self.done_page(user_id)
        with self.locks[user_id]:
            state = session.start_round()
        n = len(session.schedule)
        after = (
            "stays visible" if self.show_explanation_during_test else "will be hidden"
        )
        return _page(
            "Explanation",
            f"<p class='muted'>Round {state.plan.round_index + 1} of {n}</p>"
            "<h1>How this policy works</h1>"
            f"<div class='explanation'>{render_markdown(state.explanation.text)}</div>"
            f"{_form(user_id, 'to_test', state.plan.round_index)}"
            f"<p class='muted'>When you continue, the explanation {after}.</p>"
            "<button>I have read it, continue to the test</button></form>",
        )

    def test_page(self, user_id: str) -> bytes:
        """Two rollouts side by side, randomized order, one choice."""
        state = self.session(user_id).start_round()
        pres = state.presentation
        figures = "".join(
            f"<figure><figcaption><strong>Rollout {label}</strong></figcaption>"
            f"<img src='/bank/{quote(pres.videos[label])}' "
            f"alt='Rollout {label}'></figure>"
            for label in ("A", "B")
        )
        explanation = ""
        if self.show_explanation_during_test:
            explanation = (
                "<details><summary>Explanation</summary><div class='explanation'>"
                f"{render_markdown(state.explanation.text)}</div></details>"
            )
        return _page(
            "Which policy?",
            "<h1>Which rollout shows the explained policy?</h1>"
            "<p>Both start from the same situation. One is the policy you just "
            "read about, the other is a different policy for the same task.</p>"
            f"{explanation}<div class='videos'>{figures}</div>"
            f"{_form(user_id, 'answer', state.plan.round_index)}"
            "<p><label><input type='radio' name='answer' value='A' required> "
            "Rollout A</label> &nbsp; <label><input type='radio' name='answer' "
            "value='B'> Rollout B</label></p>"
            "<button>Submit answer</button></form>",
        )

    def feedback_page(self, user_id: str) -> bytes:
        """Satisfaction rating and optional comment."""
        state = self.session(user_id).start_round()
        reveal = ""
        if self.reveal_correctness:
            verdict = "correct" if state.correct else "incorrect"
            reveal = f"<p>Your answer was <strong>{verdict}</strong>.</p>"
        radios = " ".join(
            f"<label><input type='radio' name='rating' value='{i}' required> {i}</label>"
            for i in range(1, 6)
        )
        return _page(
            "Feedback",
            f"<h1>About the explanation</h1>{reveal}"
            "<details><summary>Show the explanation again</summary><div "
            "class='explanation'>"
            f"{render_markdown(state.explanation.text)}</div></details>"
            f"{_form(user_id, 'feedback', state.plan.round_index)}"
            f"<p>{html.escape(RATING_QUESTION)}</p><p>{radios}</p>"
            f"<p>{html.escape(TEXT_QUESTION)}<br><textarea name='text' rows='4' "
            "cols='80'></textarea></p>"
            "<button>Submit and continue</button>"
            "<p class='muted'>Please click once. Saving your feedback and preparing "
            "the next explanation can take up to a minute.</p></form>",
        )

    def done_page(self, user_id: str) -> bytes:
        """End of the session."""
        return _page(
            "Done",
            f"<h1>Thank you, {html.escape(user_id)}!</h1><p>All rounds are "
            "complete.</p>",
        )


class _Handler(BaseHTTPRequestHandler):
    app: StudyApp  # set by make_server

    def do_GET(self) -> None:  # pylint: disable=invalid-name
        """Serve pages and test videos."""
        path = urlparse(self.path).path
        try:
            if path == "/":
                self._send(self.app.start_page())
            elif path.startswith("/bank/"):
                self._send_file(path[len("/bank/") :])
            elif match := re.fullmatch(
                r"/u/([A-Za-z0-9_.-]+)/(explanation|test|feedback|done)", path
            ):
                user_id, step = match.groups()
                expected = self.app.current_step(self.app.session(user_id))
                if step != expected:
                    self._redirect(f"/u/{quote(user_id)}/{expected}")
                    return
                page = getattr(self.app, f"{step}_page")
                self._send(page(user_id))
            else:
                self.send_error(HTTPStatus.NOT_FOUND)
        except KeyError:
            self._redirect("/")
        except RuntimeError as exc:
            self.send_error(HTTPStatus.CONFLICT, str(exc))
        except Exception as exc:  # pylint: disable=broad-exception-caught
            self._send_failure(exc, "Reload this page to try again.")

    def do_POST(self) -> None:  # pylint: disable=invalid-name
        """Advance the session state machine."""
        path = urlparse(self.path).path
        length = int(self.headers.get("Content-Length", 0))
        form = {k: v[0] for k, v in parse_qs(self.rfile.read(length).decode()).items()}
        try:
            if path == "/start":
                user_id = form["user_id"].strip()
                self.app.start(user_id, form.get("condition") or None)
                self._redirect(f"/u/{quote(user_id)}/explanation")
                return
            match = re.fullmatch(
                r"/u/([A-Za-z0-9_.-]+)/(to_test|answer|feedback)", path
            )
            if not match:
                self.send_error(HTTPStatus.NOT_FOUND)
                return
            user_id, action = match.groups()
            session = self.app.session(user_id)
            with self.app.locks[user_id]:
                expected = self.app.current_step(session)
                posted_round = form.get("round")
                if (
                    session.current is None
                    or expected != ACTION_STEP[action]
                    or (
                        posted_round is not None
                        and posted_round != str(session.round_index)
                    )
                ):
                    # A double click, back button or old tab: nothing to record.
                    self.app.ctx.logger.log_event(
                        "stale_submission",
                        user_id=user_id,
                        action=action,
                        posted_round=posted_round,
                        current_round=session.round_index,
                        current_step=expected,
                    )
                    self._redirect(f"/u/{quote(user_id)}/{expected}")
                    return
                if action == "to_test":
                    session.mark_test_shown()
                    self._redirect(f"/u/{quote(user_id)}/test")
                elif action == "answer":
                    session.submit_answer(form.get("answer", ""))
                    self._redirect(f"/u/{quote(user_id)}/feedback")
                else:
                    session.submit_feedback(
                        collect_feedback(form.get("rating"), form.get("text", ""))
                    )
                    nxt = "done" if session.done else "explanation"
                    self._redirect(f"/u/{quote(user_id)}/{nxt}")
        except KeyError:
            self._redirect("/")
        except (RuntimeError, ValueError) as exc:
            self.send_error(HTTPStatus.BAD_REQUEST, str(exc))
        except Exception as exc:  # pylint: disable=broad-exception-caught
            self._send_failure(
                exc, "Go back with your browser and submit the form again."
            )

    def log_message(
        self, format: str, *args: Any  # pylint: disable=redefined-builtin
    ) -> None:  # pylint: disable=redefined-builtin
        """Quieter request logging."""

    def _send(
        self, body: bytes, content_type: str = "text/html; charset=utf-8"
    ) -> None:
        self.send_response(HTTPStatus.OK)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _send_failure(self, exc: Exception, retry_hint: str) -> None:
        """An LLM or other backend call failed; nothing was recorded, so retry works."""
        message = f"{type(exc).__name__}: {exc}"
        self.app.ctx.logger.log_event("request_error", path=self.path, error=message)
        body = _page(
            "Temporary problem",
            "<h1>Something went wrong preparing this step</h1>"
            "<p>Your previous answers are saved. Please tell the researcher.</p>"
            f"<p>{html.escape(retry_hint)}</p>"
            f"<pre class='muted'>{html.escape(message[:2000])}</pre>",
        )
        self.send_response(HTTPStatus.BAD_GATEWAY)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _send_file(self, rel: str) -> None:
        root = self.app.ctx.bank.root.resolve()
        target = (root / rel).resolve()
        if not target.is_relative_to(root) or not target.is_file():
            self.send_error(HTTPStatus.NOT_FOUND)
            return
        content_type = (
            "image/gif" if target.suffix == ".gif" else "application/octet-stream"
        )
        self._send(target.read_bytes(), content_type)

    def _redirect(self, location: str) -> None:
        self.send_response(HTTPStatus.SEE_OTHER)
        self.send_header("Location", location)
        self.end_headers()


def make_server(
    ctx: StudyContext, host: str = "127.0.0.1", port: int = 8765
) -> ThreadingHTTPServer:
    """An HTTP server bound to one study."""
    handler = type("StudyHandler", (_Handler,), {"app": StudyApp(ctx)})
    return ThreadingHTTPServer((host, port), handler)
