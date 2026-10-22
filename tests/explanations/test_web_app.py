"""Tests for the participant web interface, driven over real HTTP."""

import re
import threading
import urllib.parse
import urllib.request

import pytest

from robocode.explanations.logger import read_jsonl
from robocode.explanations.study import StudyContext
from robocode.explanations.web_app import make_server, render_markdown


def test_render_markdown_escapes_html() -> None:
    """LLM output cannot inject markup."""
    out = render_markdown("# Title\n\n- **bold** `code`\n- <script>x</script>\n\nPlain")
    assert (
        "<h2>Title</h2>" in out
        and "<strong>bold</strong>" in out
        and "<code>code</code>" in out
    )
    assert "<script>" not in out and "&lt;script&gt;" in out
    assert out.count("<ul>") == 1 and "<p>Plain</p>" in out


class _NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *args, **kwargs):  # pylint: disable=unused-argument
        """Surface redirects instead of following them."""
        return None


@pytest.fixture(name="base_url")
def fixture_base_url(ctx: StudyContext):
    """A running server on a free port."""
    server = make_server(ctx, "127.0.0.1", 0)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    yield f"http://127.0.0.1:{server.server_address[1]}"
    server.shutdown()
    server.server_close()


def _get(url: str) -> str:
    with urllib.request.urlopen(url) as resp:
        return resp.read().decode(errors="replace")


def _post(url: str, data: dict) -> str:
    opener = urllib.request.build_opener(_NoRedirect)
    req = urllib.request.Request(
        url, data=urllib.parse.urlencode(data).encode(), method="POST"
    )
    try:
        opener.open(req)
    except urllib.error.HTTPError as exc:
        if exc.code == 303:
            return exc.headers["Location"]
        raise
    raise AssertionError("expected a redirect")


def test_full_participant_flow(ctx: StudyContext, base_url: str) -> None:
    """Start, read, answer, rate for every round, then finish; rounds are logged."""
    assert "Participant ID" in _get(base_url + "/")
    loc = _post(
        base_url + "/start", {"user_id": "p01", "condition": "understanding_preference"}
    )
    assert loc == "/u/p01/explanation"
    for rnd in range(ctx.cfg.num_rounds):
        page = _get(base_url + loc)
        assert f"Round {rnd + 1} of {ctx.cfg.num_rounds}" in page
        loc = _post(base_url + "/u/p01/to_test", {})
        test_page = _get(base_url + loc)
        assert "Rollout A" in test_page and "Rollout B" in test_page
        assert (
            "How this policy works" not in test_page
        )  # explanation hidden during the test
        match = re.search(r"src='(/bank/[^']+)'", test_page)
        assert match is not None
        video = match.group(1)
        with urllib.request.urlopen(base_url + video) as resp:
            assert resp.read().startswith(b"GIF")
        loc = _post(base_url + "/u/p01/answer", {"answer": "A"})
        assert "satisfied" in _get(base_url + loc)
        loc = _post(base_url + "/u/p01/feedback", {"rating": "4", "text": "Too long."})
    assert loc == "/u/p01/done" and "Thank you" in _get(base_url + loc)
    rows = read_jsonl(ctx.logger.study_dir / "rounds.jsonl")
    assert len(rows) == ctx.cfg.num_rounds
    assert {r["feedback"]["text"] for r in rows} == {"Too long."}
    assert all(r["answer"]["reading_time_s"] is not None for r in rows)


def test_bank_files_cannot_escape_root(base_url: str) -> None:
    """Path traversal outside the test bank is refused."""
    with pytest.raises(urllib.error.HTTPError) as err:
        _get(base_url + "/bank/../../etc/passwd")
    assert err.value.code == 404


def test_invalid_rating_is_rejected(base_url: str) -> None:
    """Bad form input returns 400 and does not advance the round."""
    _post(base_url + "/start", {"user_id": "p02", "condition": "no_learning"})
    _get(base_url + "/u/p02/explanation")
    _post(base_url + "/u/p02/to_test", {})
    assert _post(base_url + "/u/p02/answer", {"answer": "B"}) == "/u/p02/feedback"
    with pytest.raises(urllib.error.HTTPError) as err:
        _post(base_url + "/u/p02/feedback", {"rating": "9"})
    assert err.value.code == 400


def test_llm_failure_shows_retryable_error_page(
    ctx: StudyContext, base_url: str, monkeypatch: pytest.MonkeyPatch
) -> None:
    """A failing explainer gives a 502 page; a reload after recovery works."""
    _post(base_url + "/start", {"user_id": "p03", "condition": "no_learning"})
    session = ctx.make_session("unused", "no_learning")  # for the generator class
    generator_cls = type(session._generator)  # pylint: disable=protected-access
    original = generator_cls.generate

    def failing(*args, **kwargs):  # pylint: disable=unused-argument
        raise ConnectionError("quota exhausted")

    monkeypatch.setattr(generator_cls, "generate", failing)
    with pytest.raises(urllib.error.HTTPError) as err:
        _get(base_url + "/u/p03/explanation")
    assert err.value.code == 502
    monkeypatch.setattr(generator_cls, "generate", original)
    assert "Round 1 of" in _get(base_url + "/u/p03/explanation")


def test_double_submit_and_stale_forms_redirect_without_error(
    ctx: StudyContext, base_url: str
) -> None:
    """Repeated or out-of-date posts go to the current step and record nothing."""
    _post(
        base_url + "/start", {"user_id": "p04", "condition": "understanding_preference"}
    )
    page = _get(base_url + "/u/p04/explanation")
    assert "name='round' value='0'" in page and "Please wait" in page
    assert _post(base_url + "/u/p04/to_test", {"round": "0"}) == "/u/p04/test"
    assert _post(base_url + "/u/p04/answer", {"answer": "A", "round": "0"}) == (
        "/u/p04/feedback"
    )
    # Double-clicked answer: already answered, so go to feedback.
    assert _post(base_url + "/u/p04/answer", {"answer": "B", "round": "0"}) == (
        "/u/p04/feedback"
    )
    feedback = {"rating": "4", "text": "ok", "round": "0"}
    assert _post(base_url + "/u/p04/feedback", feedback) == "/u/p04/explanation"
    # Double-clicked feedback: round 0 is finished, so go to the next explanation.
    assert _post(base_url + "/u/p04/feedback", feedback) == "/u/p04/explanation"
    rows = read_jsonl(ctx.logger.study_dir / "rounds.jsonl")
    assert [r["round"] for r in rows if r["user_id"] == "p04"] == [0]
    assert rows[0]["answer"]["label"] == "A"

    # Loading a later step out of order redirects instead of starting a round there.
    opener = urllib.request.build_opener(_NoRedirect)
    with pytest.raises(urllib.error.HTTPError) as err:
        opener.open(base_url + "/u/p04/feedback")
    assert err.value.code == 303 and err.value.headers["Location"] == (
        "/u/p04/explanation"
    )

    # An old round-0 form posted during round 1 is ignored, not recorded as round 1.
    _get(base_url + "/u/p04/explanation")
    _post(base_url + "/u/p04/to_test", {"round": "1"})
    _post(base_url + "/u/p04/answer", {"answer": "A", "round": "1"})
    assert _post(base_url + "/u/p04/feedback", feedback) == "/u/p04/feedback"
    rows = read_jsonl(ctx.logger.study_dir / "rounds.jsonl")
    assert [r["round"] for r in rows if r["user_id"] == "p04"] == [0]
    events = [e["event"] for e in read_jsonl(ctx.logger.study_dir / "events.jsonl")]
    assert events.count("stale_submission") == 3
