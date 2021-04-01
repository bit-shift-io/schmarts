# Schmarts
Open source cross-platform app to drive smart/IoT devices

Are you sick and tired of needing a different app to control each different smart device you own? Are you sick of the slow load times these apps make you endure through?

The objective of Schmarts is to provide a single app that lets you control all your smart devices. It aims to keep the control packets you send from phone or PC to your smart device within your own home LAN without the need to go via the cloud.

Schmarts therefore should give you some benifits:

- A single app to control your smart devices eliminating multiple control points
- Speedy load times so it is actually now quicker to load then typical smart apps which demand internet access
- Keep smart control usage free from internet/cloud and contained within your home network
- Open source so you or others can contribute

## Supported & Recommended Devices

Not all devices may support LAN mode and do require internet access. So here we have a list of recommended devices:

### Broadlink RM4 Pro
What it does: 433Mhz RF, IR blaster with learning capabilities
Supports LAN mode: YES

### Sonoff 5 relay
What it does: 5v switching relay with inching support
Supports LAN mode: YES

## Tech Stack

Python is the most popular choice for open source control of smart devices. For this reason we are predominately using python.

The Schmarts application is written using the BeeWare framework: https://beeware.org/

This allows us to support all the major platforms: Linux, Mac, Windows, Android, iOS


## Install

In tools run:

    ./install.sh

This will setup the beeware python virtual environment

# Develop

After installing, you are ready to develop:

    source beeware-venv/bin/activate
    cd app

Now run the app via:

    briefcase dev

# TODO/Wishlist

Want to contribute? Here is a list of major systems we want to possibly implement at some stage:

- Automatic device discovery
- AP mode to make the app able to connect to a smart device in AP mode and send it the wifi ssid and password
- Support for more devices
- Easy sharing/restoring of configurations
- Addition of pre-existing devices such as air conditioners, TV's
- Standard python library so other people can use what we have done outside of our app
- Plugin support
- OTA updates
- Automation/scheduling
- Web interface/cli for desktop
- Official SDK integrations


# Useful Links

## Tuya Links

https://github.com/PaulAnnekov/tuyaha
https://github.com/dev-est/tuya_tray
