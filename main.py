from tkinter import *

root = Tk()

#Defining the window
root.geometry("1280x720")
root.title("IORODEO POTENTIOSTAT")

#The menu bar (Inside root)
menubar = Menu(root)

#Options (Inside menu bar)
options = Menu(menubar, tearoff = 0)
options.add_command(label = "Device Connection")
options.add_command(label = "Test and Parameters")
options.add_command(label = "Data Acquisition")

options.add_separator()

#menubar.add_cascade(label = "Options", menu = options)

root.config(menu = options)

root.mainloop()

