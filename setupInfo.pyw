from tkinter import *
import os
import getpass
import sys
USER_NAME = getpass.getuser()

def add_to_startup(file_path=""):
    if file_path == "":
        file_path = os.path.dirname(os.path.realpath(__file__))
        print(file_path)
    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
    with open(bat_path + '\\' + "seekwifi1.bat", "w+") as bat_file:
        bat_file.write(r'start -d "%s"' % file_path + ' seek_wifi.exe')
def callback(ssid5ghz,ssid2ghz,switchAutocheck,startup):
    if startUp:
        add_to_startup(file_path="")
    ssidFile = open("ssid.txt","w")
    ssid5 = str(ssid5ghz.get())
    ssid2 =str(ssid2ghz.get())
    switchAuto =str(switchAutocheck.get())
    ssidFile.write(ssid5 + ":" + ssid2 + ":" + switchAuto)
    ssidFile.close
    root.quit()
    os.startfile('definitions.pyw')
root =Tk()
photo = PhotoImage(file = "window_icon.png")
root.iconphoto(False, photo)
root.title('Seek WiFi Setup')
ssid5ghz = StringVar()
ssid2ghz = StringVar()
switchAutocheck=StringVar()
startUp=BooleanVar()
header = Label(root, text='Seek WiFi Network Setup', font=('Bold',20), pady=20)
header.grid()
informationheader = Label(root, text='Identify the Band of your Network', font=('Bold',14), pady=20,)
informationheader.grid(row=1, column=0)
quote="A 2.4 GHz network may have 24G, 2.4, or 24 appended to the end of the network name. For example: Myhomenetwork2.4.\n A 5 GHz network may have 5G or 5 appended to the end of the network name, for example Myhomenetwork5"
information = Label(root, text=quote, font=('Bold',11), pady=20,)
information.grid(row=2, column=0)
myLabel = Label(root, text='Enter the Service Set Identifier or SSID for the 5GHz Network:', font=('Bold',13), pady=20)
myLabel.grid(row=3, column=0)
ssid5enter =Entry(root, width=45, textvariable=ssid5ghz)
ssid5enter.grid(row=3, column=1)
myLabel2 = Label(root, text="Enter the Service Set Identifier or SSID for the 2.4GHz Network:", font=('Bold',13))
myLabel2.grid(row=4, column=0)
ssid2enter =Entry(root, width=45, textvariable=ssid2ghz)
ssid2enter.grid(row=4, column=1)
switchauto = StringVar()
promptauto = Checkbutton(root, text="Switch to the fastest network automatically",font=('Bold',13), variable=switchAutocheck, onvalue='True', offvalue='')
promptauto.grid(row=7,column=1)
promptopen = Checkbutton(root, text="Open Seek WiFi on system startup",font=('Bold',13), variable=startUp, onvalue=True, offvalue=False)
promptopen.grid(row=8,column=1)

button_run= Button(root, text="Next", width=25,font=('Bold',14),command=lambda: callback(ssid5ghz,ssid2ghz,switchAutocheck,startUp))
button_run.grid(row=9, column=2)
root.mainloop()
