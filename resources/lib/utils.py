import xbmc
import xbmcaddon
import xbmcgui
import xbmcvfs

__addon_id__= 'script.toggle.local'
__Addon = xbmcaddon.Addon(__addon_id__)


def data_dir():
    return __Addon.getAddonInfo('profile')


def addon_dir():
    return __Addon.getAddonInfo('path')


def log(message, loglevel=xbmc.LOGDEBUG):
    xbmc.log(__addon_id__ + ": " + message, level=loglevel)


def showNotification(message):
    xbmcgui.Dialog().notification(getString(30010), message, time=5000, icon=xbmcvfs.translatePath(__Addon.getAddonInfo('path') + "/images/icon.png"), sound=False)


def getSetting(name):
    return __Addon.getSetting(name)


def setSetting(name, value):
    __Addon.setSetting(name,value)


def getString(string_id):
    return __Addon.getLocalizedString(string_id)


def getSettingBool(name):
    return bool(__Addon.getSettingBool(name))


def getSettingInt(name):
    return __Addon.getSettingInt(name)
