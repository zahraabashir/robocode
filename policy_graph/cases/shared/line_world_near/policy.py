# Shared example from the planning-explanations write-up: section 5.1 policy(pos, priority), instantiated as P_near with priority = 2 - x.
# Transcribed from the PDF; only quotes and line wraps were normalised.
def search(pos, priority):
    root = pos // 2
    todo = [root]
    parent = {root: None}
    while todo:
        x = min(todo, key=priority)
        todo.remove(x)
        if x == 2:
            while parent[x] is not None and parent[x] != root:
                x = parent[x]
            return 0 if x == root else x - root
        for y in (x - 1, x + 1):
            if 0 <= y < 3 and y not in parent:
                parent[y] = x
                todo.append(y)
    return 0


def policy(pos):
    return search(pos, lambda x: 2 - x)
