import zipfile, os, xbmc, xbmcgui
from resources.lib.hivemindinstaller import HivemindInstaller

if (__name__ == "__main__"):
   
    CustomizationsVersion = xbmc.getInfoLabel("System.AddonVersion(service.aw.customizations)")
    CustomizationsVersionNow = xbmc.getInfoLabel("Skin.String(CustomizationsVersion)")
    if CustomizationsVersion > CustomizationsVersionNow:
        kodi_path = '%s\\Kodi\\' % os.environ['APPDATA'] 
        dir_path = '%s\\Kodi\\addons\\service.aw.customizations\\' % os.environ['APPDATA'] 
        zip_file_path = '%scustomizations.zip' % dir_path
        zfile = zipfile.ZipFile(zip_file_path)
        zfile.extractall(kodi_path)
        zfile.close()
        xbmc.executebuiltin("Skin.SetString(CustomizationsVersion,"+str(CustomizationsVersion)+")")
    else: pass
    
    monitor = xbmc.Monitor()
    while True:             
        if monitor.waitForAbort(2):
            break
        if (xbmcgui.getCurrentWindowId() == 10000):
            HivemindInstaller()
            break