from typing import Sequence

import cli

def run(args: Sequence[str] | None = None) -> int:
    parser = cli.build_parser()
    configs = parser.parse_args()
    return 0

if __name__=="__main__":
    SystemExit(run())
