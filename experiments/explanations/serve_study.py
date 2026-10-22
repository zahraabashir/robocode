"""Serve the participant interface for a study config.

    python experiments/explanations/serve_study.py \
        --config experiments/explanations/conf/pilot.yaml [key=value ...]

Then open http://127.0.0.1:8765 . Build the test bank first
(build_test_bank.py). Sessions resume from the logs if the server restarts.
"""

import argparse
import logging

from robocode.explanations.study import StudyContext, load_config
from robocode.explanations.web_app import make_server


def main() -> None:
    """Start the HTTP server."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", required=True)
    parser.add_argument("overrides", nargs="*", help="key=value config overrides")
    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s")
    cfg = load_config(args.config, args.overrides)
    ctx = StudyContext.from_config(cfg)
    ui = cfg.get("ui", {})
    server = make_server(ctx, ui.get("host", "127.0.0.1"), int(ui.get("port", 8765)))
    host, port = str(server.server_address[0]), server.server_address[1]
    print(f"Serving study {cfg.study_id} at http://{host}:{port}  (Ctrl-C to stop)")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
