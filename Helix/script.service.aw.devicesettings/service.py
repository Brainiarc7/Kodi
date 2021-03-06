try:
    import time
    import xbmc
    import xbmcgui
    import AlphaUIUtils

    def writeHomeWindowSetting(key, value):
        win = xbmcgui.Window(10000)
        win.setProperty(key, value)
 
    if __name__ == '__main__':
        monitor = xbmc.Monitor()

        while True:                
            try:
                writeHomeWindowSetting("IsHDMIInCableConnected",str(AlphaUIUtils.IsHDMICableConnected()))
            except:
                writeHomeWindowSetting("IsHDMIInCableConnected","False")     

            # Sleep/wait for abort for 10 seconds
            if monitor.waitForAbort(3):
                # Abort was requested while waiting. We should exit
                break
except:
    pass