"""Explicit execution adapters, including RoboCode's existing episode lifecycle."""

from __future__ import annotations

import importlib.abc
import importlib.machinery
import inspect
import sys
from contextlib import contextmanager
from pathlib import Path

from .instrument import compile_source
from .recognition import Recognition
from .recorder import Frame, Recorder
from .scoring import report

_active_session = None


class _Loader(importlib.abc.Loader):
    def __init__(self, recorder, file):
        self.recorder, self.file = recorder, Path(file)

    def create_module(self, spec):
        return None

    def exec_module(self, module):
        """Execute a sibling module inside its own provenance frame."""
        code, name = compile_source(
            self.recorder, self.file, self.file.read_text(encoding="utf-8")
        )
        module.__dict__[name] = self.recorder
        old = self.recorder.frame
        self.recorder.frame = Frame(None, self.recorder.next_invocation)
        self.recorder.next_invocation += 1
        try:
            exec(code, module.__dict__)  # pylint: disable=exec-used
        finally:
            self.recorder.frame = old


class _Finder(importlib.abc.MetaPathFinder):
    def __init__(self, recorder, root):
        self.recorder, self.root = recorder, root

    def find_spec(
        self, fullname, path=None, target=None
    ):  # pylint: disable=unused-argument
        """Replace only loaders of Python modules inside the policy directory."""
        spec = importlib.machinery.PathFinder.find_spec(fullname, path)
        if (
            spec
            and spec.origin
            and spec.origin.endswith(".py")
            and Path(spec.origin).resolve().is_relative_to(self.root)
        ):
            spec.loader = _Loader(self.recorder, spec.origin)
            return spec
        return None


class RuntimeSession:
    """One policy and its persistent history. Use as a context manager.

    ``call`` labels arguments as observation sources explicitly. ``get_action``
    returns are action sinks by default; other adapters can use ``action=True``.
    Import hooks are process-global: sessions are synchronous and non-concurrent.
    """

    def __init__(self, path, config=None):
        self.path = Path(path).resolve()
        self.recorder = Recorder(config)
        self.policy = None
        self.namespace = {}
        self.phase_counts = {}
        self.metadata = {}
        self.old_path = []
        self.old_modules = {}
        self.finder = None
        self.semantic_adapter = None

    def __enter__(self):
        global _active_session  # pylint: disable=global-statement
        if _active_session is not None:
            raise RuntimeError(
                "RuntimeSession requires exclusive use; another session is active"
            )
        root = self.path.parent
        self._structural_hints()
        self.old_path = list(sys.path)
        self.old_modules = dict(sys.modules)
        siblings = {p.stem for p in root.glob("*.py")} | {
            p.name for p in root.iterdir() if (p / "__init__.py").is_file()
        }
        for name in list(sys.modules):
            if name.split(".")[0] in siblings:
                del sys.modules[name]
        sys.path.insert(0, str(root))
        self.finder = _Finder(self.recorder, root)
        sys.meta_path.insert(0, self.finder)
        _active_session = self
        return self

    def _structural_hints(self):
        self.recorder.recognition = Recognition(self.path)
        self.recorder.structural_sites = self.recorder.recognition.loop_sites()

    def __exit__(self, exc_type, exc, tb):
        global _active_session  # pylint: disable=global-statement
        if exc is not None:
            self.recorder.graph.incomplete = f"{type(exc).__name__}: {exc}"
        sys.meta_path.remove(self.finder)
        sys.path[:] = self.old_path
        for name, module in list(sys.modules.items()):
            file = getattr(module, "__file__", None)
            if file and Path(file).resolve().is_relative_to(self.path.parent):
                if name in self.old_modules:
                    sys.modules[name] = self.old_modules[name]
                else:
                    sys.modules.pop(name, None)
        for name, module in self.old_modules.items():
            if name not in sys.modules:
                sys.modules[name] = module
        _active_session = None

    def source_transform(self, source, path):
        """Compilation hook for RoboCode's existing source validation and loader."""
        code, name = compile_source(self.recorder, path, source)
        return code, {name: self.recorder}

    def load(self, class_name=None, constructor_args=(), constructor_kwargs=None):
        """Execute the module and optionally construct its policy class."""
        with self.phase("load"):
            code, injected = self.source_transform(
                self.path.read_text(encoding="utf-8"), self.path
            )
            self.namespace = {
                "__file__": str(self.path),
                "__name__": "_policy_graph_policy",
                **injected,
            }
            exec(code, self.namespace)  # pylint: disable=exec-used
        if class_name is None and "GeneratedApproach" in self.namespace:
            class_name = "GeneratedApproach"
        if class_name is not None:
            with self.phase("construction"):
                cls = self.namespace[class_name]
                if self.semantic_adapter is not None:
                    self.policy = cls(*constructor_args, **(constructor_kwargs or {}))
                    return self
                self.policy = self.recorder.call(
                    self.recorder.harness_site,
                    self.recorder.external(cls),
                    [self.recorder.external(a) for a in constructor_args],
                    {
                        k: self.recorder.external(v)
                        for k, v in (constructor_kwargs or {}).items()
                    },
                ).value
        return self

    @contextmanager
    def phase(self, name):
        """Record the boundaries and completion status of one lifecycle call."""
        r = self.recorder
        old = r.phase
        count = self.phase_counts.get(name, 0)
        self.phase_counts[name] = count + 1
        r.phase = f"{name}:{count}"
        start = len(r.graph.events)
        phase = r.phase
        try:
            yield
        except BaseException as exc:
            r.graph.incomplete = f"{type(exc).__name__}: {exc}"
            raise
        finally:
            r.calls.append(
                {"phase": phase, "start_event": start, "end_event": len(r.graph.events)}
            )
            r.phase = old

    def call(self, name, *args, state_args=(0,), action=None, **kwargs):
        """Invoke a function or method with explicit observations and action sinks."""
        r = self.recorder
        fn = (
            getattr(self.policy, name)
            if self.policy is not None
            else self.namespace[name]
        )
        with self.phase(name):
            if self.semantic_adapter is not None:
                return self.semantic_adapter.call(
                    fn,
                    args,
                    kwargs,
                    state_args=state_args,
                    action=action if action is not None else name == "get_action",
                )
            values = [
                r.external(a, state=i in state_args, name=f"{name}.arg{i}")
                for i, a in enumerate(args)
            ]
            keywords = {
                k: r.external(v, state=k in state_args, name=f"{name}.{k}")
                for k, v in kwargs.items()
            }
            function = r.external(fn, name=name)
            if inspect.ismethod(fn):
                function.receiver = r.external(self.policy, name="self")
            result = r.call(r.harness_site, function, values, keywords)
            is_action = action if action is not None else name == "get_action"
            if is_action:
                r.actions.append(r.event("action", r.harness_site, [result.ref]))
            return result.value

    def report(self, *, include_graph=False):
        """Return JSON-compatible scores and optionally the complete event graph."""
        result = report(self.recorder, self.metadata, include_graph=include_graph)
        if self.semantic_adapter is not None:
            self.semantic_adapter.summarize(result)
        return result

    def run_episode(self, env, *, seed=0, max_steps=100, primitives=None, count=None):
        """Trace an environment episode, retaining partial evidence on failure."""
        _trace_episode(
            self,
            env,
            seed=seed,
            max_steps=max_steps,
            primitives=primitives,
            count=count,
        )
        return self


def trace_episode(
    path, env, *, seed=0, max_steps=100, primitives=None, config=None, count=None
):
    """Use RoboCode's loader and run_episode; environment ownership stays with caller.

    RoboCode dependencies are imported only for this adapter. Small fixtures and
    the graph itself need only the standard library.
    """
    return RuntimeSession(path, config).run_episode(
        env, seed=seed, max_steps=max_steps, primitives=primitives, count=count
    )


def _trace_episode(session, env, *, seed, max_steps, primitives, count):
    # Optional dependencies stay lazy so standalone source fixtures need no gym.
    # pylint: disable=import-outside-toplevel
    from robocode.approaches.base_approach import BaseApproach
    from robocode.utils.episode import load_generated_approach, run_episode

    session.metadata.update(
        {
            "seed": seed,
            "max_steps": max_steps,
            "object_count": count,
            "environment": str(getattr(env, "spec", None)),
        }
    )
    with session:
        with session.phase("load-and-construction"):
            session.policy = load_generated_approach(
                session.path,
                env.action_space,
                env.observation_space,
                primitives or {},
                source_transform=session.source_transform,
            )

        # solve_instance is an optional per-instance API, unused by run_episode.
        class Adapter(BaseApproach):  # pylint: disable=abstract-method
            """Bridge the existing episode driver to the traced policy instance."""

            def reset(self, state, info):
                super().reset(state, info)
                session.call("reset", state, info)

            def _get_action(self):
                return session.call("get_action", self._last_state)

            def update(self, state, reward, done, info):
                super().update(state, reward, done, info)
                if hasattr(session.policy, "update"):
                    session.call("update", state, reward, done, info)

        adapter = Adapter(
            env.action_space, env.observation_space, seed, primitives or {}
        )
        metrics, _, _ = run_episode(env, adapter, seed, max_steps, count=count)
        session.metadata["episode_metrics"] = metrics
