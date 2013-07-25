import xbmcgui
import xbmcvfs
import xbmc
import resources.lib.utils as utils

class Toggle:
    REMOTE_MODE = 0;
    LOCAL_MODE = 1;
    
    def run(self):
        mode = xbmcgui.Dialog().select(utils.getString(30010),[utils.getString(30011),utils.getString(30012)])

        copyComplete = True
        if(mode == self.REMOTE_MODE):
            copyComplete = self._copyFile(utils.getSetting('remote_filename'))
        elif(mode == self.LOCAL_MODE):
            copyComplete = self._copyFile(utils.getSetting('local_filename'))

        
        if(copyComplete):
            #prompt the user to restart xbmc
            restartXbmc = xbmcgui.Dialog().ok(utils.getString(30010),"",utils.getString(30013))

    def _copyFile(self,filename):
        utils.log("copying " + filename + " to advancedsettings.xml")

        if(xbmcvfs.exists(xbmc.translatePath(filename))):
            advanced_settings = xbmc.translatePath('special://profile/advancedsettings.xml')

            #if advancedsettings already exists, delete it
            if(xbmcvfs.exists(advanced_settings)):
                xbmcvfs.delete(advanced_settings)

            #copy the new file
            xbmcvfs.copy(xbmc.translatePath(filename),advanced_settings)
            
            return True
        else:
            xbmcgui.Dialog().ok(utils.getString(30010),utils.getString(30014))
            
            return False


Toggle().run()
