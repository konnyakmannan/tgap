from typing import Sequence

import cli

def run(args: Sequence[str] | None = None) -> int:
    parser = cli.build_parser()
    configs = parser.parse_args()
    if hasattr(configs, 'func'):
        result = configs.func(configs)
        print(result)
    else:
        parser.print_help()
        return 1
    return 0

if __name__=="__main__":
    SystemExit(run())
