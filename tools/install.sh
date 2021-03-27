#!/bin/bash

# install deps
# https://docs.beeware.org/en/latest/tutorial/tutorial-0.html

# set up a virtual environment for beeware
cd ..


cd app/src/schmarts
rm -rf sonoffLAN
git clone git@github.com:AlexxIT/SonoffLAN.git
mv SonoffLAN/custom_components/sonoff sonoffLAN2
rm -rf SonoffLAN
mv sonoffLAN2 sonoffLAN
cd ../../..

python3 -m venv beeware-venv


# activate the virtual environment
source beeware-venv/bin/activate

# install deps into the virtual env
python -m pip install briefcase
python -m pip install broadlink
python -m pip install pysonofflan

# for AlexxIT/SonoffLAN.git
python -m pip install homeassistant
python -m pip install pycrypto
python -m pip install zeroconf

# start a new project from scratch:
#   source beeware-venv/bin/activate
#   briefcase new

# https://docs.beeware.org/en/latest/tutorial/tutorial-5/android.html
# briefcase create android
# briefcase build android
# briefcase run android

# https://docs.beeware.org/en/latest/tutorial/tutorial-5/iOS.html
# briefcase create iOS
# briefcase build iOS
# briefcase run iOS -d "iPhone 11"
