#!/bin/bash

cd ..
source beeware-venv/bin/activate
cd app
briefcase update # create involked if scaffolding doesn't exist (https://docs.beeware.org/en/latest/tutorial/tutorial-4.html)
briefcase build

# build the installer
briefcase package --no-sign

# if you want to run the app:
briefcase run