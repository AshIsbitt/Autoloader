import sys

# Function to create JSON file


# Function to write to JSON


# Function to read/print out JSON


# Function to open all listed locations in JSON


# Function for dashboard to give users input options
def main():
    print('AUTOLOADER')
    print("Enter 'r' to run, or 'm' to manage stored locations. Enter 'x' to exit")
    entry = input(">>> ")

    try:
        if entry.lower() == 'r':
            run()
        elif entry.lower() == 'm':
            print('/nManage saved locations')
            print("'v': View saved locations")
            print("'a': Add new location")
            print("'r': Remove saved location")
            print("'e': Erase all")
            print("'x': Return to main menu")
            manageEntry = input(">>> ")

            if manageEntry.lower() == 'v':
                pass
            elif manageEntry.lower() == 'a':
                pass
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
        print("Error, unknown command")
        sys.exit


if __name__ == '__main__':
    main()
