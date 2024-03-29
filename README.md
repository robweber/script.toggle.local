# Toggle Local
[![Build Status](https://img.shields.io/travis/com/robweber/script.toggle.local)](https://app.travis-ci.com/github/robweber/script.toggle.local)
[![License](https://img.shields.io/github/license/robweber/script.toggle.local)](https://github.com/robweber/script.toggle.local/blob/master/LICENSE.txt)
[![PEP8](https://img.shields.io/badge/code%20style-pep8-orange.svg)](https://www.python.org/dev/peps/pep-0008/)

__Kodi Version Compatibility:__ Kodi 17.x (Krypton) and greater

This script was created for a very specific need I had from some of my Kodi clients. Specifically for tablet and phone installations I have the following two use cases:

1. using them at home and needing access to the home network sources and mysql database
2. using them away from home and wanting access to local database and sources only

## Install

There are no outside dependencies, other than Kodi's main libraries, so you can download and install using the zip file from this repo.

## Usage

This addon can toggle between these two states by renaming advancedsetting.xml files and restarting Kodi. Currently you need two files:

* advancedsettings.local.xml
* advancedsettings.remote.xml

When running the addon you can select which "state" you want your Kodi instance to be a part of. This will remove the current advancedsettings.xml information and rename the correct file. Once Kodi is restarted your new settings will take place.

## Attributions

Folder Icon by [Jojo Mendoza](https://www.iconfinder.com/hopstarter) - [Creative Commons Attribution-NonCommercial 3.0 Unported license](https://creativecommons.org/licenses/by-nc/3.0/legalcode)

## License
[MIT](/LICENSE)
