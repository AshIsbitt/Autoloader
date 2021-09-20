import sys
import os
import json
import pyinputplus as pyplus

SAVED_FILE = 'autoloader.json'

# Run function to open all stored location
def runAutoLoad():
    pass

# function to read JSON and print all options to screen
def viewJSONDoc():
    with open(SAVED_FILE, 'r') as jsonFile:
        jsonData = json.load(jsonFile)

    for key, value in jsonData.items():
        print(f'{key}: {value}')

    main()

# Function to append new item to JSON
def addNewEntry():
    with open(SAVED_FILE, 'r') as jsonFile:
        jsonData = json.load(jsonFile)
        print(jsonData)


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

    # Add item to list in JSON Dict
    jsonData[newLocType].append(newLoc)

    with open(SAVED_FILE, 'w') as jsonFile:
        json.dump(jsonData, jsonFile)

    print('Item added')

    main()

# Function to remove item from JSON
def removeEntry():
    pass


# Function to delete JSON page
def deleteJSON():
    verifyFunc = pyplus.inputYesNo(
        'Are you sure you want to delete the config file? ')

    if verifyFunc == 'yes':
        print('Deleting file...')
        os.remove(SAVED_FILE)

    sys.exit()



# Create new JSON
def createJSONFile():
    datadict = {}
    datadict['web'] = []
    datadict['app'] = []
    datadict['dir'] = []

    with open(SAVED_FILE, 'w') as JsonFile:
        json.dump(datadict, JsonFile)


# Function for dashboard to give users input options
def main():
    print('AUTOLOADER')

    if not os.path.isfile(SAVED_FILE):
        createJSONFile()
        print('Initialising new document')

    print("Enter 'r' to run, or 'm' to manage stored locations. Enter 'x' to exit")
    entry = input(">>> ")

    try:
        if entry.lower() == 'r':
            runAutoLoad()
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
                addNewEntry()
            elif manageEntry.lower() == 'r':
                removeEntry()
            elif manageEntry.lower() == 'e':
                deleteJSON()
            elif manageEntry.lower() == 'x':
                main()

        elif entry.lower() == 'x':
            print('Goodbye')

    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
