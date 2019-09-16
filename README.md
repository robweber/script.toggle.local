script.toggle.local
===================

[![Build Status](https://travis-ci.org/robweber/script.toggle.local.svg?branch=master)](https://travis-ci.org/robweber/script.toggle.local/)

__Kodi Version Compatibility:__ Kodi 16.x (Jarvis) and greater

This script was created for a very specific need I had from some of my Kodi clients. Specificically for tablet and phone installations I have the following two use cases: 

1. using them at home and needing access to the home network sources and mysql database
2. using them away from home and wanting access to local database and sources only 

This addon can toggle between these two states by renaming advancedsetting.xml files and restarting Kodi. Currently you need two files: 

* advancedsettings.local.xml
* advancedsettings.remote.xml

When running the addon you can select which "state" you want your Kodi instance to be a part of. This will remove the current advancedsettings.xml information and rename the correct file. Once Kodi is restarted your new settings will take place.


### Attributions

Folder Icon by (Jojo Mendoza)[https://www.iconfinder.com/hopstarter] - (Creative Commons Attribution-NonCommercial 3.0 Unported license)[https://creativecommons.org/licenses/by-nc/3.0/legalcode]
