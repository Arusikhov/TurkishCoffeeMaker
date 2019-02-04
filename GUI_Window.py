#Andrew Beechko
#CSE 308 Project GUI
#Last Edited 2-3-19

from tkinter import *
from PIL import Image, ImageTk



#------------------------------------
#Test Data
Sstate = "Brewing"
Scolor = "green"
Estate = "Good"
Ecolor = "green"

endstat = "false"

temp = 80
weight = 10
#-------------------------------------
#Functions


def eightozcheck(): #Making the State label depend on button selection, temperature, weight, and vibration
    while endstat != "true":
        if temp < 90:
            StateTxt.config(text = "Brewing", bg = "yellow")
        elif 90 <temp <105:
            StateTxt.config(text = "Ready", bg = "green")
        elif temp > 105:
            StateTxt.config(text = "Not Ready", bg = "red")
        if weight < 7.5:
            StateTxt.config(text = "Not Ready", bg = "red")
            ErrorTxt.config(text = "Add Water")
        elif weight > 8.5:
            StateTxt.config(text="Not Ready", bg ="red")
            ErrorTxt.config(text = "Remove Water")
        elif 7.5 < weight < 8.5:
            ErrorTxt.config(text = "Good")


def tenozcheck():
    while endstat != "true":
        if temp < 90:
            StateTxt.config(text="Brewing", bg ="yellow")
        elif 90 < temp < 105:
            StateTxt.config(text="Ready", bg ="green")
        elif temp > 105:
            StateTxt.config(text="Not Ready", bg ="red")
        if weight < 9.5:
            StateTxt.config(text = "Not Ready", bg = "red")
            ErrorTxt.config(text = "Add Water")
        elif weight > 10.5:
            StateTxt.config(text="Not Ready", bg ="red")
            ErrorTxt.config(text = "Remove Water")
        elif 9.5 < weight < 10.5:
            ErrorTxt.config(text = "Good")
def twelveozcheck():
    while endstat != "true":
        if temp < 90:
            StateTxt.config(text="Brewing", bg="yellow")
        elif 90 < temp < 105:
            StateTxt.config(text="Ready", bg="green")
        elif temp > 105:
            StateTxt.config(text="Not Ready", bg="red")
        if weight < 11.5:
            StateTxt.config(text="Not Ready", bg="red")
            ErrorTxt.config(text="Add Water")
        elif weight > 12.5:
            StateTxt.config(text="Not Ready", bg="red")
            ErrorTxt.config(text="Remove Water")
        elif 11.5 < weight < 12.5:
            ErrorTxt.config(text="Good")
def endpress():
    endstat = "true"


#------------------------------------
#Window program
Window = Tk()
Window.geometry("400x400")
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
eightozB.place(x = 40, y = 80)

tenozB = Button(Window, text = "10oz", width = 6, font = 20, bg = "cyan", command = tenozcheck)
tenozB.place(x = 160, y = 80)

twelveozB = Button(Window, text = "12oz", width = 6, font = 20, bg = "cyan", command = twelveozcheck)
twelveozB.place(x = 280, y = 80)

endB = Button(Window, text = "End", width = 6, font = 20, bg = "red", command = endpress)
endB.place(x = 0, y = 0)

#Placing objects
StateTxt.place(x=40, y= 200)
ErrorTxt.place(x = 20, y = 320)
TopTxt.pack(side = TOP)

Pic = Label(Window, image = photo)
Pic.image = photo
Pic.pack()
Pic.place(x= 160, y = 160)
Window.mainloop()