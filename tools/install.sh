#!/bin/bash

# install deps
# https://docs.beeware.org/en/latest/tutorial/tutorial-0.html

# set up a virtual environment for beeware
cd ..

python3 -m venv beeware-venv

# activate the virtual environment
source beeware-venv/bin/activate

# install deps into the virtual env
python -m pip install briefcase

# start a new project from scratch:
#   source beeware-venv/bin/activate
#   briefcase new