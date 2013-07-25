script.toggle.local
===================

This script was created for a very specific need I had from some of my xbmc clients. Specificically for tablet and phone installations I have the following two use cases: 

1. using them at home and needing access to the home network sources and mysql database
2. using them away from home and wanting access to local database and sources only 

This addon can toggle between these two states by renaming advancedsetting.xml files and restarting xbmc. Currently you need two files: 

* advancedsettings.local.xml
* advancedsettings.remote.xml

When running the addon you can select which "state" you want your xbmc instance to be a part of. This will remove the current advancedsettings.xml information and rename the correct file. Once xbmc is restarted your new settings will take place. 
