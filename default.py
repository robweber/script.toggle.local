import xbmcgui
import xbmcvfs
import xbmc
import json
import resources.lib.utils as utils

class Toggle:
    REMOTE_MODE = 0
    LOCAL_MODE = 1
    UNKNOWN_MODE = 2
    
    fileLoc = xbmc.translatePath(utils.data_dir() + "mode.json")
    jsonObj = None
    
    def __init__(self):
        #load the current mode
        self._openFile()
    
    def run(self):

        currentMode = {
            self.REMOTE_MODE: utils.getString(30011),
            self.LOCAL_MODE: utils.getString(30012),
            self.UNKNOWN_MODE: utils.getString(30023)
        }
        
        if(xbmcgui.Dialog().yesno(utils.getString(30010), utils.getString(30024), currentMode[self.jsonObj['mode']], utils.getString(30025))):
        
            mode = xbmcgui.Dialog().select(utils.getString(30010),[utils.getString(30011),utils.getString(30012)])
            
            copyComplete = False
            if(mode == self.REMOTE_MODE):
                copyComplete = self._copyFile(utils.getSetting('remote_filename'))
            elif(mode == self.LOCAL_MODE):
                copyComplete = self._copyFile(utils.getSetting('local_filename'))
    
            
            if(copyComplete):
                self.jsonObj['mode'] = mode
                self._writeFile()
                
                #prompt the user to restart xbmc
                restartXbmc = xbmcgui.Dialog().yesno(utils.getString(30010),"",utils.getString(30013))
    
                if(restartXbmc):
                    
                    #on windows just restart the app
                    if(xbmc.getCondVisibility('System.Platform.Windows')):
                        xbmc.executebuiltin('RestartApp()')
                    else:
                        xbmc.restart();

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
        
    def _openFile(self):
        if(xbmcvfs.exists(self.fileLoc)):
            f = xbmcvfs.File(self.fileLoc)
            
            self.jsonObj = json.loads(f.read())
            
            f.close()
            
        else:
            self.jsonObj = {"mode":self.UNKNOWN_MODE}
            
    def _writeFile(self):
        
        #make the data dir if it doesn't exist
        if(not xbmcvfs.exists(utils.data_dir())):
            xbmcvfs.mkdir(utils.data_dir())
        
        f = xbmcvfs.File(self.fileLoc,'w')
        
        f.write(json.dumps(self.jsonObj))
        
        f.close()


Toggle().run()
