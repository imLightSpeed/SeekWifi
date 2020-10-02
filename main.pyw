import os
runAlready=os.path.isfile('ssid.txt')
if runAlready:
    os.startfile('definitions.pyw')
else:
   os.startfile('setupInfo.pyw')
