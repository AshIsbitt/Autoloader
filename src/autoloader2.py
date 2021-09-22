import argparse
import pprint as pp
from typing import Sequence
from typing import Optional
import json

def runAutoLoad():
    print('Running')

def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers(dest='command')

    # Single command parsers
    runParser = subparser.add_parser('run')
    viewParser = subparser.add_parser('view')
    eraseParser = subparser.add_parser('erase')

    # Parsers requiring arguments
    addParser = subparser.add_parser('add')
    remParser = subparser.add_parser('rem')

    addParser.add_argument('-c', '--category', type=str, required=True)
    addParser.add_argument('-l', '--location', type=str, required=True)

    remParser.add_argument('-c', '--category', type=str, required=True)
    remParser.add_argument('-l', '--location', type=str, required=True)

    # Get arguments given
    args = parser.parse_args(argv)

    # print given arguments
    pp.pprint(vars(args))

    if args.command == 'run':
        runAutoLoad()
    elif args.command == 'view':
        pass
    elif args.command == 'erase':
        pass
    elif args.command == 'view':
        pass
    elif args.command == 'add':
        pass
    elif args.command == 'rem':
        pass

if __name__=='__main__':
    exit(main())
