# Autoloader

A short script that opens a list of predefined websites, applications, and file manager locations with the intention of running when you first start up your computer - better suited to laptops, but able to run on desktops too.

Version 1.0 of this script was designed when I was in college, and only worked on windows. This repo hold a completely rewritten version that should work on all operating systems.

### Install
`git clone git@github.com:AshIsbitt/Autoloader.git`

Also make sure you install the python requirements as well.

`pip3 install requirements.txt`

### How to use
Each command starts with `python3 autoloader.py ...` in the terminal.

* `run` - Autoloader opens the configured locations in the default web browser/file browser, and opens configured software.
* `view` - Displays all configured apps, directory locations, and websites
* `add` - Add new location to the config
    * `-c` or `--category` - (Required) Set category. Available options include "web" for websites, "dir" for directory locations, and "app" for applications.
    * `-l` or `--location` - (Required) Set specific location. Use absolute paths where relevant
* `rem` - Remove location from config
    * `-c` or `--category` - (Required) Set category. Available options include "web" for websites, "dir" for directory locations, and "app" for applications.
    * `-l` or `--location` - (Required) Set specific location. Use absolute paths where relevant
* `erase` - Erase entire config file. A new blank file will be initialised next time you run a command.
