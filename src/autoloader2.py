import argparse
import pprint as pp
from typing import Sequence
from typing import Optional
import json

def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser()

    # Run or manage
    parser.add_argument('function', type=str,
         help="Run or manage saved locations. Functions: ['run', 'view', 'add', 'rem', 'erase']")

    # Get arguments given
    args = parser.parse_args(argv)

    # print given arguments
    pp.pprint(vars(args))

    if args.function.lower() == 'run':
        return('running')
    elif args.function.lower() == 'add':
        return('adding')
    elif args.function.lower() == 'rem':
        pass
    elif args.function.lower() == 'erase':
        pass
    elif args.function.lower() == 'view':
        pass
    else:
        return('Invalid function. Run -h for help')


if __name__=='__main__':
    exit(main())
