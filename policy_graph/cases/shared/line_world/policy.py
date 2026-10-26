# Shared example from the planning-explanations write-up: Appendix A.2 (examples/line_world/policy.py), the FIFO search P_FIFO of section 5.
# Transcribed from the PDF; only quotes and line wraps were normalised.
def policy(pos):
    root = pos // 2
    todo = [root]
    parent = {root: None}

    while todo:
        x = todo.pop(0)

        if x == 2:
            # Follow parents back to the first step.
            while parent[x] is not None and parent[x] != root:
                x = parent[x]
            return 0 if x == root else x - root

        for y in (x - 1, x + 1):
            if 0 <= y < 3 and y not in parent:
                parent[y] = x
                todo.append(y)

    return 0
