#Andrew Beechko
#CSE 308 Project GUI
#Last Edited 2-5-2019

from tkinter import *
from PIL import Image, ImageTk
import time
from threading import Thread
#---------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
#functions


def combine_funcs(*funcs):#an attempt to have one button trigger multiple functions
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func

def raise_frame(frame):#is used to toggle between frames
    frame.tkraise()


def guithread():
    athread = Thread(target=myGUI)
    athread.setDaemon(True)
    athread.start()


#-------------------------------------------------------------------------------------

class myGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("MyGUI")
        #---------------------------
        #the dictionary
        f = open("DataFile.txt")
        lines = f.readlines()
        f.close()

        MyDictionary = {
            "NWweight": int(lines[1]),
            "Wweight": int(lines[2]),
            "SenseWeight": int(lines[0]),
            "Temperature": int(lines[3]),
            "Vibration": int(lines[4]),
            "EndBStat": lines[5]
        }

        #-------------------------------------------------------
        #Functions


        def recordclickNW(self):#the record button
            sweight = MyDictionary["SenseWeight"]
            if sweight < 20:
                self.ErrorTxt2.config(text = "No Jazzve Detected")
            else:
                sweight = str(sweight)
                # opening files

                NWfile = open('Data_No_Water.txt', "r")
                NWfiledata = NWfile.read()  # read in line from file
                NWfile.close()
                Newfiledata = NWfiledata.replace(NWfiledata, sweight)  # replacing text
                f = open("Data_No_Water.txt", "w")
                f.write(Newfiledata)
                f.close()
                self.ErrorTxt2.config(text="No Water Weight Recorded")

        def recordclickW(self):#the record button
            sweight = MyDictionary["SenseWeight"]
            if sweight < 20:
                self.ErrorTxt2.config(text = "No Jazzve Detected")
            else:
                sweight = str(sweight)
                # opening files

                Wfile = open('Data_With_Water.txt', "r")
                Wfiledata = Wfile.read()  # read in line from file
                Wfile.close()
                Newfiledata = Wfiledata.replace(Wfiledata, sweight)  # replacing text
                f = open("Data_With_Water.txt", "w")
                f.write(Newfiledata)
                f.close()
                self.ErrorTxt2.config(text="With Water Weight Recorded")

        def EndBtoggle(self):#turns EndBStat to 1 which is ment to end the induction controll loop
            MyDictionary["EndBStat"] = "True"
            self.StateTxt.config(text = "idle", bg = "yellow")
            self.ErrorTxt1.config(text = "End Press", bg = "green")


        def StartButtonF(self):  # button command def
            if MyDictionary["NWweight"] > MyDictionary["SenseWeight"]:  # checks to see if weight is within the range of the button
                self.StateTxt.config(text="Idle", bg="yellow")
                self.ErrorTxt1.config(text="Missing Jazzve", bg="red")
            elif MyDictionary["NWweight"] < MyDictionary["SenseWeight"] < MyDictionary["Wweight"] - 5:
                self.StateTxt.config(text="Idle", bg="yellow")
                self.ErrorTxt1.config(text="Add Water", bg="red")
            elif MyDictionary["SenseWeight"] > MyDictionary["Wweight"] + 5:
                self.StateTxt.config(text="Idle", bg="yellow")
                self.ErrorTxt1.config(text="Too Heavy", bg="red")
            elif MyDictionary["Wweight"] - 5 < MyDictionary["SenseWeight"] < MyDictionary["Wweight"] + 5:  # if weight is in range, starts our loop
                MyDictionary["EndBStat"] = 0
                InductionThread(self)

        def InductionAuto(self):  # need to make this a thread, checks temp and vib and toggles induction bassed off of these
            while MyDictionary["EndBStat"] == 0:  # checks endB and if it is 0, runs the loop
                # Turn on the induction heater
                if MyDictionary["Temperature"] < 200:
                    self.ErrorTxt1.config(text=" ", bg="green")
                    self.StateTxt.config(text="Brewing", bg="yellow")
                elif MyDictionary["Temperature"] > 200:
                    if MyDictionary["Vibration"] == 1:
                        self.ErrorTxt1.config(text=" ", bg="green")
                        self.StateTxt.config(text="Ready", bg="green")
                        #turn off induction heater

        #def updateDict(self):





        #Threads
        '''
        def updateThread(self):
            athread = Thread(target = updateDict(self))
            athread.setDaemon(True)
            athread.start()
        '''

        def InductionThread(self):  # this turns the StartButtonF into a thread in order to run in parallel
            mythread = Thread(target=InductionAuto(self))  # assigns the button to the thread
            mythread.setDaemon(True)
            mythread.start()
        #---------------------------------------------------------------------------------------------------------

        self.master.geometry("480x320")

        self.f1 = Frame(self.master)  # putting frame in the main window module
        self.f2 = Frame(self.master)

        for frame in (self.f1, self.f2):  # assigning dimensions of frame and making it the size of the window
            frame.place(x=0, y=0, relheight=1, relwidth=1)  # (x,y) topL corner position, (relh,w) seting proportion relative to parent object
            frame.configure(bg="black")
        #-----------------------------------------------------------------------------
        # f1 widgets

        self.TopTxt = Label(self.f1, text="The Perfect Brew", relief=RIDGE, bg="cyan", font=20, width=16)
        self.TopTxt.pack(side=TOP)

        self.StartB = Button(self.f1, text="Start", width=8, font=40, bg="cyan", command= lambda: StartButtonF(self))
        self.StartB.place(x=190, y=70)

        self.EndB = Button(self.f1, text="End", width=8, font=40, bg="cyan", command=lambda: EndBtoggle(self))
        self.EndB.place(x = 360, y = 70)

        self.ConfigB = Button(self.f1, text="Configure", width=8, font=40, bg="cyan", command=lambda: raise_frame(self.f2))
        self.ConfigB.place(x = 20, y = 70)

        self.StateLabel = Label(self.f1,text = "State:", fg = "white", bg = "black", width = 8, font = 40)
        self.StateLabel.place(x = 10, y = 240)
        self.StateTxt = Label(self.f1, relief=RIDGE, bg="green", text="Waiting", font=20, width=8)
        self.StateTxt.place(x = 90, y = 240)

        self.ErrorLabel = Label(self.f1, text = "Error:", fg = "white", bg = "black", width = 8, font = 40)
        self.ErrorLabel.place(x = 10, y = 280)
        self.ErrorTxt1 = Label(self.f1, relief=RIDGE, bg="green", text=" ", font=20, width=12)
        self.ErrorTxt1.place(x = 90, y = 280)

        self.TempLabel = Label(self.f1, text = "Temperature:", fg = "white", bg = "black", width = 11, font = 40)
        self.TempLabel.place(x = 20, y = 130)
        self.TempDisp = Label(self.f1, text = MyDictionary["Temperature"], fg = "white", bg = "black", width = 4, font = 40)
        self.TempDisp.place(x = 155, y = 130)

        self.WeightLabel = Label(self.f1, text = "Sensor Weight:", fg = "white", bg = "black", width = 12, font = 40 )
        self.WeightLabel.place(x = 20, y = 170)
        self.WeightDisp = Label(self.f1, text = MyDictionary["SenseWeight"], fg = "white", bg = "black", width = 4, font = 40)
        self.WeightDisp.place(x = 155, y = 170)

        #Picture
        im = Image.open("TurkishCoffeMakerImage.png")
        photo = ImageTk.PhotoImage(im)
        self.Pic = Label(self.f1, image=photo)
        self.Pic.image = photo
        self.Pic.place(x=280, y=120)
        # ----------------------------------------------------------------------------------------------------------------
        # f2 widgets

        self.ConfigBack = Button(self.f2, text="Go Back", width=8, font=40, bg="cyan", command=lambda: raise_frame(self.f1))
        self.ConfigBack.place(x = 40, y = 40)

        self.RecordBNW = Button(self.f2, text="Empty Jazzve", width=14, font=40, bg="cyan", command=lambda: recordclickNW(self))
        self.RecordBNW.place(x = 220, y = 20)

        self.RecordBW = Button(self.f2, text = "Full Jazzve", width=14, font=40, bg="cyan", command = lambda: recordclickW(self))
        self.RecordBW.place(x = 220, y = 70)

        self.ErrorTxt2 = Label(self.f2, relief=RIDGE, bg="yellow", text=" ", font=20, width=25)
        self.ErrorTxt2.place(x = 100, y = 280)

        self.InstrTxt = Label(self.f2, relief=RIDGE,fg = "white", bg="black",wraplength = 260, text="This Window is used to Configure your coffee maker. Once you have the Jazzve prepared, put it in the coffee maker and press the relavent button.", font=15, width=25)
        self.InstrTxt.place(x = 100, y = 120)


        raise_frame(self.f1)
        #updateThread(self)




root = Tk()
my_gui = myGUI(root)
guithread()
root.mainloop()



