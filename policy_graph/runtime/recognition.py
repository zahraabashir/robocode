"""Reuse baseline semantic rules, with execution witnesses instead of static labels.

This is a compatibility boundary around the frozen classifier's private API.
Static candidates include discarded computations; relevance is decided exclusively
by the runtime dependency graph. A source match alone is never a witness.

Candidates are collected over all nodes so that discarded work is visible. The
baseline applies one rule only to its action slice: a look-ahead choice whose
winner reaches the action combined with the current state is a target choice,
not action planning (``_encodes``). That rejection is applied here too, against
the decision function's slice, for candidates found from any entrypoint.

A look-ahead whose winner is outside the static action slice is kept, because
discarded work is still performed planning, but the rule could not be checked.
Its matches are marked ``action_slice_rules: "unchecked"``; scoring does not let
such a match alone establish action-relevant planning.

The reset classifier exists to recognize reset-time (cached) planning with
reset's observation as the state. Its candidates must lie in code reset runs;
code reached only from the decision function is judged by that classifier.
"""

import time

from policy_graph.depgraph import build_graph
from policy_graph.reactivity import PolicyConfig, _Classifier, discover_entrypoint

# pylint: disable=protected-access

ROLE_KINDS = {
    "prediction": {"transition", "operation", "call-return"},
    "choice": {"choice", "condition", "call-return"},
    "orderings": {"call-return"},
    "ranking": {"choice"},
    "feasibility check": {"call-return"},
    "recursive call": {"call-return"},
    "search loop": {"structural-candidate"},
    "expansion": {"call-return"},
}


class Recognition:
    """Static rule candidates and their required, executed operations."""

    def __init__(self, path):
        self.evidence = []
        self.rejected = []
        self.unchecked = set()  # Look-aheads the action-slice rules never saw.
        self.choice_calls = set()
        self.error = None
        started = time.perf_counter()
        try:
            graph = build_graph([path])
            decision, _ = discover_entrypoint(graph)
            entrypoints = {decision} | {
                name
                for name, function in graph.functions.items()
                if not function.is_lambda and function.node.name == "reset"
            }
            seen = set()
            classifiers = {
                entrypoint: _Classifier(graph, entrypoint, PolicyConfig())
                for entrypoint in sorted(entrypoints)
            }
            action = classifiers[decision]
            action.all_nodes = set(graph.nodes)
            for entrypoint, classifier in classifiers.items():
                classifier.all_nodes = action.all_nodes
                choices = classifier._choices(classifier.all_nodes)
                for choice in choices:
                    call = graph.call_sites.get(choice.site)
                    if call is not None:
                        self.choice_calls.add(
                            (choice.file, choice.line, call.ast_node.col_offset)
                        )
                # Keep the baseline unchanged; test this private API boundary.
                for evidence in classifier._evidence(
                    classifier.all_nodes, record=False
                ):
                    key = (evidence.kind, evidence.file, evidence.line, evidence.what)
                    if key in seen:
                        continue
                    seen.add(key)
                    reason = (
                        None
                        if entrypoint == decision
                        else self._outside_entrypoint(graph, entrypoint, evidence)
                    ) or self._slice_rejection(classifier, action, choices, evidence)
                    if reason:
                        self.rejected.append(
                            {
                                "rule": evidence.kind,
                                "file": evidence.file,
                                "line": evidence.line,
                                "entrypoint": entrypoint,
                                "reason": reason,
                            }
                        )
                    else:
                        self.evidence.append(evidence)
                        if evidence.kind == "lookahead" and not (
                            set(evidence.winners) & action.slice
                        ):
                            self.unchecked.add(id(evidence))
        except (ValueError, SyntaxError, OSError) as exc:
            self.error = f"{type(exc).__name__}: {exc}"
        self.seconds = time.perf_counter() - started
        self._sites = {}
        for evidence in self.evidence:
            for role, file, line in evidence.sites:
                if role != "action":
                    self._sites.setdefault((file, line), set()).update(
                        ROLE_KINDS.get(role, set())
                    )
        self._lines = {(e.file, e.line) for e in self.evidence}
        self._applicable = {}
        # Required (role, file, line, kinds) per candidate, in evidence order.
        self.roles = [
            [
                (role, file, line, ROLE_KINDS.get(role, set()))
                for role, file, line in evidence.sites
                if role != "action"
            ]
            for evidence in self.evidence
        ]
        self._functions = {
            e.function.rsplit(".", 1)[-1]
            for e in self.evidence
            if e.kind in ("tree-search", "generate-and-test", "graph-search")
        }

    @staticmethod
    def _outside_entrypoint(graph, entrypoint, evidence):
        """A role site in a function the classifier's entrypoint never calls."""
        reachable = graph.reachable_functions(entrypoint)
        scopes = {}
        for node in graph.nodes:
            scopes.setdefault((node.file, node.line), set()).add(node.scope)
        for role, file, line in evidence.sites:
            if role != "action" and not scopes.get((file, line), set()) & reachable:
                return (
                    f"{role} site at line {line} is not executed by {entrypoint}; "
                    "the decision function's classifier applies there"
                )
        return None

    @staticmethod
    def _slice_rejection(classifier, action, choices, evidence):
        """The baseline's action-slice rejection of a look-ahead (see module doc)."""
        if evidence.kind != "lookahead":
            return None
        winners = set(evidence.winners)
        if not winners & action.slice:
            return None  # Discarded or unrelated to the action: kept as performed.
        for choice in choices:
            if (choice.file, choice.line) != (evidence.file, evidence.line) or set(
                choice.winners
            ) != winners:
                continue
            _, models, rolls = classifier._predictions(choice)
            if not models and not rolls and not action._encodes(choice.winners):
                return (
                    "target choice: the chosen candidate reaches the action combined "
                    "with the current state (baseline _encodes rule)"
                )
        return None

    def loop_sites(self):
        """Mark actual iterations, not evaluation of an empty loop's header."""
        return {
            (file, line): evidence.kind
            for evidence in self.evidence
            if evidence.kind == "graph-search"
            for role, file, line in evidence.sites
            if role == "search loop"
        }

    def witness_kinds(self):
        """Event kinds that can witness some role at each (file, line)."""
        return self._sites

    def applicable(self, event):
        """Cheap necessary conditions for ``match`` to return a recognition."""
        if event.detail.get("contract_internal") or event.detail.get(
            "instrumented_callee"
        ):
            return False
        if event.kind == "call-return":
            return (
                event.site.file,
                event.site.line,
                event.site.column,
            ) in self.choice_calls and (event.site.file, event.site.line) in self._lines
        return (
            event.site.file,
            event.site.line,
        ) in self._lines or event.site.function.rsplit(".", 1)[-1] in self._functions

    def applicable_evidence(self, event):
        """Indices of candidates whose site/function filters admit this event."""
        if not self.applicable(event):
            return ()
        key = (event.kind, event.site.file, event.site.line, event.site.function)
        if key not in self._applicable:
            self._applicable[key] = tuple(
                i
                for i, evidence in enumerate(self.evidence)
                if self._admits(evidence, event)
            )
        return self._applicable[key]

    @staticmethod
    def _admits(evidence, event):
        if event.kind == "call-return" and evidence.kind not in (
            "lookahead",
            "ordering-search",
        ):
            return False
        if evidence.kind in ("planner-call", "transition-model"):
            return False  # Already handled by runtime API contracts.
        if evidence.kind in ("lookahead", "ordering-search") and (
            event.site.file != evidence.file or event.site.line != evidence.line
        ):
            return False
        if evidence.kind in ("tree-search", "generate-and-test", "graph-search"):
            # Scope names omit the module prefix used by the static graph.
            return evidence.function.endswith("." + event.site.function)
        return True

    def describe(self, index, role_ids):
        """The recognition record for candidate ``index`` and its witnesses."""
        evidence = self.evidence[index]
        return {
            "basis": "baseline structural heuristic with execution witnesses",
            "rule": evidence.kind,
            "description": evidence.what,
            "assumptions": evidence.assumptions,
            "witness_ids": sorted({i for ids in role_ids.values() for i in ids}),
            "role_witness_ids": role_ids,
            "action_slice_rules": (
                "unchecked" if id(evidence) in self.unchecked else "applied"
            ),
        }

    def match(self, graph, event, scope):
        """Require related operation witnesses in this decision's dynamic slice.

        Opaque bodies do not prove their hidden statements executed. Call-return
        witnesses establish calls, never the internal operations of those calls.
        All returned IDs are real trace events, not synthetic static nodes.
        """
        if not self.applicable(event):
            return None
        hits = [
            i
            for i in scope | {event.id}
            if graph.events[i].kind
            in self._sites.get(
                (graph.events[i].site.file, graph.events[i].site.line), ()
            )
            and not graph.events[i].detail.get("contract_internal")
        ]
        checked = any(
            graph.events[i].kind in ("comparison", "call-return") for i in scope
        )
        return self.match_witnesses(graph, event, hits, checked)

    def match_witnesses(self, graph, event, hits, checked):
        """``match`` given the witness-site events in the slice and whether it
        contains a comparison or call-return."""
        by_site = {}
        for i in hits:
            witness = graph.events[i]
            by_site.setdefault((witness.site.file, witness.site.line), []).append(
                witness
            )
        for evidence in self.evidence:
            if event.kind == "call-return" and evidence.kind not in (
                "lookahead",
                "ordering-search",
            ):
                continue
            if evidence.kind in ("planner-call", "transition-model"):
                continue  # Already handled by runtime API contracts.
            if evidence.kind in ("lookahead", "ordering-search") and (
                event.site.file != evidence.file or event.site.line != evidence.line
            ):
                continue
            if evidence.kind in ("tree-search", "generate-and-test", "graph-search"):
                # Scope names omit the module prefix used by the static graph.
                if not evidence.function.endswith("." + event.site.function):
                    continue
            witnesses = []
            roles = {}
            required = []
            for role, file, line in evidence.sites:
                if role == "action":
                    continue  # Static entrypoint is not an executed action witness.
                kinds = ROLE_KINDS.get(role, set())
                found = [w.id for w in by_site.get((file, line), []) if w.kind in kinds]
                required.append(bool(found))
                witnesses.extend(found)
                roles.setdefault(role, []).extend(found)
            if required and all(required):
                # A control decision must actually depend on a comparison/check.
                if event.kind == "condition" and not checked:
                    continue
                return {
                    "basis": "baseline structural heuristic with execution witnesses",
                    "rule": evidence.kind,
                    "description": evidence.what,
                    "assumptions": evidence.assumptions,
                    "witness_ids": sorted(set(witnesses)),
                    "action_slice_rules": (
                        "unchecked" if id(evidence) in self.unchecked else "applied"
                    ),
                    "role_witness_ids": roles,
                }
        return None
