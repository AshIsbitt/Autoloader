import argparse
import pprint as pp
from typing import Sequence
from typing import Optional
import json
import os
import pyinputplus as pyplus
import webbrowser
import platform
import subprocess
import getpass as gp

SAVED_FILE = 'autoloader_config.json'

def createJSONFile():
    dataDict = {}
    dataDict['web'] = []
    dataDict['app'] = []
    dataDict['dir'] = []

    with open(SAVED_FILE, 'w') as JsonFile:
        json.dump(dataDict, JsonFile)

def runAutoLoad():
    with open(SAVED_FILE, 'r') as jsonFile:
        jsonData = json.load(jsonFile)

    for value in jsonData['web']:
        print(value)
        webbrowser.open(f'https://{value}')

    for value in jsonData['app']:
        if str(platform.platform())[0:5] == 'macOS':
            if value[-4:] != '.app':
                value += '.app'

            if os.path.exists(f'/System/Applications/{value}'):
                subprocess.Popen(['open', f'/System/Applications/{value}'])
            else:
                subprocess.Popen(['open', f'/Applications/{value}'])

        elif str(platform.platform())[0:6] == 'Windows':
            subprocess.Popen('explorer "' + value + '"')
        else:
            print("Please submit the following message on the github repo: https://github.com/AshIsbitt/Autoloader/issues")
            print(f"Operating system not supported: {platform.platform()}")


    for value in jsonData['dir']:
        subprocess.call(['open', '-R', value])

def viewJSONDoc():
    with open(SAVED_FILE, 'r') as jsonFile:
        jsonData = json.load(jsonFile)

    for key, value in jsonData.items():
        print(f'{key}: {value}')

    return jsonData.items()

def eraseJSONFile():
    verify = pyplus.inputYesNo(
        """Are you sure you want to completely erase the config file.
This action cannot be undone. """)

    if verify == 'yes':
        print('Deleting config...')
        os.remove(SAVED_FILE)

def addItemToJson(category, item):
    with open(SAVED_FILE, 'r') as jsonFile:
        jsonData = json.load(jsonFile)

    jsonData[category].append(item)

    with open(SAVED_FILE, 'w') as jsonFile:
        json.dump(jsonData, jsonFile)

    return(f'{item} added to {category} category')

def removeItemFromJson(category, item):
    with open(SAVED_FILE, 'r') as jsonFile:
        jsonData = json.load(jsonFile)

    jsonData[category].remove(item)

    with open(SAVED_FILE, 'w') as jsonFile:
        json.dump(jsonData, jsonFile)

    return(f'{item} removed from {category} category')

def main(argv: Optional[Sequence[str]] = None) -> int:
    if not os.path.isfile(SAVED_FILE):
        createJSONFile()
        print('Creating new config file')

    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers(dest='command')

    # Single command parsers
    runParser = subparser.add_parser('run', help='Execute all saved locations in Autoloader')
    viewParser = subparser.add_parser('view', help='Display locations in config file')
    eraseParser = subparser.add_parser('erase', help='Erase config file')

    # Parsers requiring arguments
    addParser = subparser.add_parser('add', help='Add item to config')
    remParser = subparser.add_parser('rem', help='Remove item from config')

    addParser.add_argument('-c', '--category', type=str, required=True, help="Type of location to save. Options are 'web', 'app' 'dir'")
    addParser.add_argument('-l', '--location', type=str, required=True, help='Location ie website or file location to add')

    remParser.add_argument('-c', '--category', type=str, required=True, help="Type of location to remove. Options are 'web', 'app' 'dir'")
    remParser.add_argument('-l', '--location', type=str, required=True, help='Location ie website or file location to remove')

    # Get arguments given
    args = parser.parse_args(argv)

    # print given arguments
    pp.pprint(vars(args))

    if args.command == 'run':
        runAutoLoad()
    elif args.command == 'view':
        viewJSONDoc()
    elif args.command == 'erase':
        eraseJSONFile()
    elif args.command == 'add':
        if args.category not in ['web', 'app', 'dir']:
            print("Invalid category. Options: 'web', 'app', 'dir'")
        else:
            print(addItemToJson(args.category, args.location))
    elif args.command == 'rem':
        if args.category not in ['web', 'app', 'dir']:
            print("Invalid category. Options: 'web', 'app', 'dir'")
        else:
            print(removeItemFromJson(args.category, args.location))

if __name__=='__main__':
    exit(main())

