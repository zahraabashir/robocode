# Shared example from the planning-explanations write-up: Appendix A.1 (examples/line_world_reactive/policy.py).
# Transcribed from the PDF; only quotes and line wraps were normalised.
def policy(pos):
    return 1 if pos < 4 else 0
