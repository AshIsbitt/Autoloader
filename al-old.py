#! python3

'''
Programmed by Ash Isbitt
version_number = 4.1x
Latest Update - 06/07/2016
'''

from time import *
from sys import *
import os
import subprocess

'''
This subroutine opens the text file in read mode.
FOR every line in the file, it reads the first three letters and then runs
specific commands to open the specific file or URL entered.

The sub also uses a TRY statement to make sure that the file exists. If it
doesnt exist, then the user is alerted of this, and directed to the
setup subroutine
'''
def Run():
    try:
        fr = open('AutoLoader.txt', 'r')
            
        for line in (line.rstrip() for line in fr.readlines()):
            if line[0:3] == 'web':
                #open in the browser
                os.startfile(line[3:])
            elif line[0:3] == 'loc':
                cmd = line[3:]
                subprocess.Popen('explorer "' + cmd + '"')
            elif line[0:2] == "--":
                next
            else:
                process = subprocess.Popen(line)
       
        fr.close()
    
    except FileNotFoundError:
        print("Program not setup")
        print("Running setup\n")
        Setup()
        
'''
This subroutine starts by opening a new file in 'append' mode
It then loops through a series of statements that asks the user
to input anything they want to load up during the program's runtime
'''        
def Setup():
    fw = open('AutoLoader.txt', 'a')

    x = True
    
    while x == True:
        print("Enter new location to add to file")
        print("Enter e to cancel")
        print("Start with 'loc' for file location")
        new_entry = str(input("Start with 'web' if it's a web page\n"))

        if new_entry == 'e' or new_entry == 'E':
            Start()
        else:
            fw.write(new_entry)
            fw.write('\n')
        
        y = input('New Data? Y/N\n')

        if y == 'N' or y == 'n':
            fw.close()
            break
            
    fw.close()
    Start()

def remove():
    f = open('AutoLoader.txt', 'r')
    lines = f.readlines()
    f.close()

    f = open('AutoLoader.txt', 'w')

    ToDel = input("Enter location to remove\n")

    for line in lines:
        if line.contains() != ToDel:
            f.write(line)

    f.close()
    print("Successful\n")
    Start()


def View():
    f = open('AutoLoader.txt', 'r')
    lines = f.readlines()

    for line in lines:
        print(line)

    f.close()
    print()
    manage()
    
def manage():
    print("Manage")
    print("Enter s to setup file")
    print("Enter a to erase file")
    print("Enter r to remove from the file")
    print("Enter v to view the current files")
    print('Enter e to return to the main menu')
    ent = input()

    if ent.upper() == 'S':
        Setup()
    if ent.upper() == 'A':
        os.remove("AutoLoader.txt")
    if ent.upper() == 'R':
        remove()
    if ent.lower() == 'v':
        View()
    if ent.lower() == 'e':
        Start()
        

'''
Start here.
This function gets input from the user for which mode to run
and then uses the IF statement to decide which subroutine above
to run based on that input
'''
def Start():
    print("AUTOLOADER")
    print("Enter r to run")
    print("Enter m to manage the file")
    entry = input("Enter e to exit\n")

    if entry == 'r' or entry == 'R':
        Run()
    elif entry.upper() == 'M':
        manage()
    elif entry == 'e' or entry == 'E':
        print("Goodbye")
        exit
    else:
        print('ERROR')
        sleep(1)
        exit

Start()
