#Andrew Beechko
#CSE 308 Project GUI
#Last Edited 2-3-19

from tkinter import *
from PIL import Image, ImageTk
import time



#------------------------------------
#Test Data
weight = 8

temp = 80
#------------------------------------
#Window program
Window = Tk()

eozB = 0
tozB = 0
twozB = 0

#----------------------------------------------------------------------------
#Functions
def eightozcheck():  # Making the State label depend on button selection, temperature, weight, and vibration
    global temp
    if weight < 7.5:
        StateTxt.config(text="Not Ready", bg="red")
        ErrorTxt.config(text="Add Water", bg="red")
    elif weight > 8.5:
        StateTxt.config(text="Not Ready", bg="red")
        ErrorTxt.config(text="Remove Water", bg="red")
    elif 7.5 < weight < 8.5:
        ErrorTxt.config(text=" ", bg="green")
        StateTxt.config(text="Brewing", bg="yellow")
        if temp < 95:
            global eozB
            eozB = 1
            temp += 1
            print("temp increased")
            Window.after(100, eightozcheck)
        else:
            eozB = 0
            StateTxt.config(text="Ready", bg="green")
            print("temp done")

def tenozcheck():
        global temp
        global tozB
        if weight < 9.5:
            StateTxt.config(text = "Not Ready", bg = "red")
            ErrorTxt.config(text = "Add Water", bg = "red")
        elif weight > 10.5:
            StateTxt.config(text="Not Ready", bg ="red")
            ErrorTxt.config(text = "Remove Water", bg = "red")
        elif 9.5 < weight < 10.5:
            ErrorTxt.config(text = "Good", bg = "green")
            StateTxt.config(text = "Brewing", bg = "yellow")
            if temp < 95:
                tozB = 1
                temp+=1
                print("temp increased ", temp)
                Window.after(100, tenozcheck)
            else:
                tozB = 0
                StateTxt.config(text = "Ready", bg = "green")
                print("Temp done")


def twelveozcheck():
    if weight < 11.5:
        StateTxt.config(text="Not Ready", bg="red")
        ErrorTxt.config(text="Add Water", bg="red")
    elif weight > 12.5:
        StateTxt.config(text="Not Ready", bg="red")
        ErrorTxt.config(text="Remove Water", bg="red")
    elif 11.5 < weight < 12.5:
        ErrorTxt.config(text="Good", bg="green")
        StateTxt.config(text = "Brewing", bg = "yellow")
        if temp < 95:
            global twozB
            twozB = 1
            temp += 1
            print("Temp increased ", temp)
            Window.after(100, twelveozcheck)
        else:
            twozB = 0
            StateTxt.config(text = "Ready", bg = "green")
            print("Temp done")
#--------------------------------------------------------------------
Window.geometry("480x320")
Window.configure(background = 'black')

#Immage
im = Image.open("TurkishCoffeMakerImage.png")
photo = ImageTk.PhotoImage(im)

#Lables
StateTxt = Label(Window, relief = RIDGE,bg = "green", text = "Waiting", font = 20, width = 8)

ErrorTxt = Label(Window, relief = RIDGE,bg = "green", text = " ", font = 20, width = 12 )

TopTxt = Label(Window, text = "The Perfect Brew", relief = RIDGE, bg = "cyan", font = 20, width = 16)

#Buttons

eightozB = Button(Window, text = "8oz", width = 6, font = 20, bg = "cyan", command = eightozcheck)
eightozB.place(x = 10, y = 60)

nineozB = Button(Window, text = "9oz", width = 6, font = 20, bg = "cyan")
nineozB.place(x=90, y = 60)

tenozB = Button(Window, text = "10oz", width = 6, font = 20, bg = "cyan", command = tenozcheck)
tenozB.place(x = 170, y = 60)

elevenozB = Button(Window, text = "11oz", width = 6, font = 20, bg = "cyan")
elevenozB.place(x = 250, y = 60)

twelveozB = Button(Window, text = "12oz", width = 6, font = 20, bg = "cyan", command = twelveozcheck)
twelveozB.place(x = 330, y = 60)

endB = Button(Window, text = "STOP", width = 6, font = 20, bg = "red")
endB.place(x= 410, y=60)
#endB = Button(Window, text = "End", width = 6, font = 20, bg = "red", command = endpress)
#endB.place(x = 0, y = 0)

#Placing objects
StateTxt.place(x=40, y= 160)
ErrorTxt.place(x = 20, y = 220)
TopTxt.pack(side = TOP)

Pic = Label(Window, image = photo)
Pic.image = photo
Pic.pack()
Pic.place(x= 220, y = 100)

#trying to use after function to recursively call the eightozcheck function
if eozB == 1:
    Window.after(1000, eightozcheck)

Window.mainloop()