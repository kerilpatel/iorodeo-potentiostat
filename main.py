import tkinter as tk
from tkinter import *
from tkinter import ttk


#creating parent window
root = tk.Tk()
root.title("IORODEO POTENTIOSTAT")

#adding tabs to the parent window
tabcontrol = ttk.Notebook(root)

#creating tabs
tab1 = ttk.Frame(tabcontrol)
tab2 = ttk.Frame(tabcontrol)
tab3 = ttk.Frame(tabcontrol)

#adding tab
tabcontrol.add(tab1, text = "Device Connection")
tabcontrol.add(tab2, text = "Test and Parameters")
tabcontrol.add(tab3, text = "Data Acquisition")

tabcontrol.pack(expand = 1, fill = "both")

#creating example labels inside the tabs
ttk.Label(tab1, text="This is the Device Connection tab").grid(column = 0, row = 0, padx = 360, pady = 360)
ttk.Label(tab2, text = "This is the test and parameters tab").grid(column = 0, row = 0, padx = 360, pady = 360)
ttk.Label(tab3, text = "This is the data acquisition tab").grid(column = 0, row = 0, padx = 360, pady = 360)

root.mainloop()
