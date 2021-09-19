import sys
import os
import json

SAVED_FILE = 'autoloader.json'

# Function to create JSON file
def createJSONfile():
    jsonFile = open(SAVED_FILE, 'x')
    return jsonFile

# Function to write to JSON
def addItemToJSON():
    try:
        with open(SAVED_FILE, 'rb') as jsonFile:
            jsonRaw = json.load(jsonFile)
    except FileNotFoundError:
        jsonRaw = json.load(createJSONfile())

    print('file created/exist')

    print('Enter type of location:')
    print("'web': Website location")
    print("'app': Local software to run")
    print("'dir': Directory location to open in file explorer")

    newLocType = input('>>> ')

    if newLocType.lower() not in ['web', 'app', 'dir']:
        print('Try again\n')
        addItemToJSON()

    print("Enter location (If 'app' or 'dir', make sure you use absolute locations)")
    newLoc = input(">>> ")

    jsonEntry = {f"{newLocType}": f"{newLoc}"}

    jsonRaw.append(jsonEntry)

    with open(SAVED_FILE, 'w') as jsonFile:
        json.dump(jsonRaw)
# Function to read/print out JSON
def viewJSONDoc():
    jsonRaw = json.loads(SAVED_FILE)

    for key, value in jsonRaw:
        print(f'({key}), {value}')

    print('\n')

# Function to open all listed locations in JSON


# Function for dashboard to give users input options
def main():
    print('AUTOLOADER')
    print("Enter 'r' to run, or 'm' to manage stored locations. Enter 'x' to exit")
    entry = input(">>> ")

    try:
        if entry.lower() == 'r':
            pass
        elif entry.lower() == 'm':
            print('\nManage saved locations')
            print("'v': View saved locations")
            print("'a': Add new location")
            print("'r': Remove saved location")
            print("'e': Erase all")
            print("'x': Return to main menu")
            manageEntry = input(">>> ")

            if manageEntry.lower() == 'v':
                viewJSONDoc()
            elif manageEntry.lower() == 'a':
                addItemToJSON()
            elif manageEntry.lower() == 'r':
                pass
            elif manageEntry.lower() == 'e':
                pass
            elif manageEntry.lower() == 'x':
                main()

        elif entry.tolower() == 'x':
            print('Goodbye')
            sys.exit
    except:
        print('Error')
        sys.exit()

if __name__ == '__main__':
    main()
