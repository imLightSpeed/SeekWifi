from tkinter import *
import time
import multiprocessing
import os
from win10toast import ToastNotifier
import getpass
import subprocess
USER_NAME = getpass.getuser()
toaster = ToastNotifier()
def runwifi():
        def runSetup():
            info = open("ssid.txt",'r')
            doc = ""
            doclines = info.readlines()
            for line in doclines:
                doc = doc + line.replace(" ", "");
            firstColon=doc.index(":")
            secondColonstart=firstColon+1
            secondColonlocation=doc.index(":", secondColonstart)
            thirdColonstart=secondColonlocation+1
            ssid5 = str(doc[:firstColon])
            ssid2 = str(doc[secondColonstart:secondColonlocation])
            switchAuto = doc[thirdColonstart:]
            return ssid5,ssid2,switchAuto;
        def network(ssid5,ssid2):
            signalStrength = "Netsh wlan show networks mode=bssid"
            dataByte = subprocess.check_output(signalStrength)
            data = dataByte.decode("utf-8")
            #get signal for 5ghz network
            find5=data.find(ssid5)
            findsignal5 = data.find("Signal",find5)
            findcolon5 = data.find(":", findsignal5)
            start5=findcolon5 + 2
            end5= findcolon5 + 4
            sig5 = data[start5:end5]
            #get signal for 2.4ghz network
            find2=data.find(ssid2)
            findsignal2 =data.find("Signal",find2)
            findcolon2 = data.find(":", findsignal2)
            start2=findcolon2 + 2
            end2= findcolon2 + 4
            sig2 = data[start2:end2]
            #interface 5
            interface= "netsh WLAN show interfaces"
            currentByte = subprocess.check_output(interface)
            network = currentByte.decode("utf-8")
            on5 = network.find(ssid5)
            #interface 24
            on2 = network.find(ssid2)
            return sig5,sig2,on5,on2;
        def antiSpam(spamLevel):
            #x is proritty level greater number means importyant function
            if spamLevel == 1:
           #     print("short cooldown")
                time.sleep(150)
            if spamLevel ==2:
             #   print("long Cooldown")
                time.sleep(300)
        def switch(networkID):
            switchTo ='netsh wlan connect ssid='+ networkID +' name='+networkID
            subprocess.call(switchTo)
        ssid5,ssid2,switchAuto = runSetup()
        ssid5=str(ssid5)
        ssid2=str(ssid2)
        switchAutobool=bool(switchAuto)
        switchAuto=switchAutobool
        toaster = ToastNotifier()
        while True:
            sig5,sig2,on5,on2 = network(ssid5,ssid2)
            
            try:
                id2 = int(sig2)
            except:
                sig2 = 1
            try:
                id5 = int(sig5)
            except:
                sig5 = 1
            if sig5==1 or sig2==1:
                if sig5==1 and sig2==1:
                    toaster.show_toast("Seek WiFi","No known networks are currently available",duration=15)
                    antiSpam(1)
                if sig5==1 and on2==-1:
                #if we can't find a signal to ssid5 and we aren't connected to the 2.4, prompt to switch
                    if switchAuto: 
                        toaster.show_toast("Seek WiFi","Switching to " + ssid2 + ", " + ssid5 + " is not reachable",duration=15)
                        switch(ssid2)
                        antiSpam(2)
                    else:
                        toaster.show_toast("Seek WiFi","Switch to " + ssid2 + ", " + ssid5 + " is not reachable",duration=15)
                if sig2==1 and on5==-1:
                    if not switchAuto:
               
                        toaster.show_toast("Seek WiFi","Switching to " + ssid5 + ", " + ssid2 + " is not reachable",duration=15)
                        switch(ssid5)
                        antiSpam(2)
                    else:
                        toaster.show_toast("Seek WiFi","Switch to " + ssid5 + ", " + ssid2 + " is not reachable",duration=15)
                time.sleep(180)
                continue
                
            if switchAuto:
                if id5 == id2 and on5 == -1:
                    toaster.show_toast("Seek WiFi","Switching to " + ssid5 + ", it is stronger",duration=15)
                    switch(ssid5)
                    antiSpam(2)
                else:
                    if id5 < 30 and on2 != -1:
                        toaster.show_toast("Seek WiFi","Switching to " + ssid2 + ", it is stronger",duration=15)
                        switch(ssid2)
                        antiSpam(1)
                    if id5 > 30 and on5 == -1:
                        toaster.show_toast("Seek WiFi","Switching to " + ssid5 + ", it is stronger",duration=15)
                        switch(ssid5)
                        antiSpam(2)
            else:
                if id5 == id2 and on5 == -1:
                    toaster.show_toast("Seek WiFi","Switch to " + ssid5 + ", it is stronger",duration=15)
                    antiSpam(1)
                else:
                    if id5 < 30 and on2 != -1:
                        toaster.show_toast("Seek WiFi","Switch to " + ssid2 + ", it is stronger",duration=15)
                        antiSpam(1)
                    if id5 > 30 and on5 == -1:
                        toaster.show_toast("Seek WiFi","Switch to " + ssid5 + ", it is stronger",duration=15)
                        antiSpam(1)
            time.sleep(180)
i = multiprocessing.Process(target=runwifi)

if __name__=='__main__':
    def reset():
        os.remove("ssid.txt")
        runOnstart=os.path.isfile(r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\seekwifi.bat' % USER_NAME)
        if runOnstart:
            os.remove(r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\seekwifi.bat' % USER_NAME)
        quit()
    def info():
        info = open("ssid.txt",'r')
        doc = ""
        doclines = info.readlines()
        for line in doclines:
            doc = doc + line.replace(" ", "");
        firstColon=doc.index(":")
        secondColonstart=firstColon+1
        secondColonlocation=doc.index(":", secondColonstart)
        thirdColonstart=secondColonlocation+1
        ssid5 = str(doc[:firstColon])
        ssid2 = str(doc[secondColonstart:secondColonlocation])
        switchAuto = doc[thirdColonstart:]
        return ssid5,ssid2,switchAuto;
    def wifi():
        i.start()
        def switch():
            if button_run["state"] == "normal":
                button_run["state"] = "disabled"
            else:
                button_run["state"] = "normal"
        switch()
        ssid5,ssid2,switchAuto =info()
        switchAuto =bool(switchAuto)
        information = Label(root, text='Seek WiFi is running and will contine to monitor your network...', font=('Bold',12), pady=20,)
        information.grid(row=2, column=0)
        ssid5 = Label(root,text ='5GHz Network: '+ssid5,font=('Bold',12), pady=20,)
        ssid5.grid(row=3,column=0)
        ssid2 = Label(root,text ='2.4GHz Network: '+ssid2,font=('Bold',12), pady=20,)
        ssid2.grid(row=4,column=0)
        if switchAuto:
            switch = Label(root,text ='Seek WiFi is switching networks automatically',font=('Bold',12), pady=20,)
            switch.grid(row=5,column=0)
        else:
            switch = Label(root,text ='Seek WiFi is not switching networks automatically',font=('Bold',12), pady=20,)
            switch.grid(row=5,column=0)    
    def quit():
        if i.is_alive():
            i.terminate()
        root.destroy()


    root =Tk()
    root.title('Seek WiFi')
    photo = PhotoImage(file = "window_icon.png")
    root.iconphoto(False, photo)
    header = Label(root, text='Seek WiFi', font=('Bold',20), pady=20)
    header.grid()
    button_run= Button(root, text="Start Seek WiFi", width=25,font=('Bold',11),command=wifi)
    button_run.grid(row=6, column=1)
    button_reset= Button(root, text="Reset Network Information", width=25,font=('Bold',11),command=reset)
    button_reset.grid(row=6, column=2)
    button_exit= Button(root, text="Quit Seek WiFi", width=25,font=('Bold',11),command=quit)
    button_exit.grid(row=6, column=3)

    root.mainloop()
