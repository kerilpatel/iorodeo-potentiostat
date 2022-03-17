import tkinter as tk
from tkinter import *
from tkinter import ttk

import TestAndParameters
import graph

#creating parent window
root = tk.Tk()
root.title("IORODEO POTENTIOSTAT")
root.geometry("720x720")

#adding tabs to the parent window
tabcontrol = ttk.Notebook(root)

#creating main tabs
deviceConnectionTab = ttk.Frame(tabcontrol)
testAndParametersTab = ttk.Frame(tabcontrol)
dataAcquisitionTab = ttk.Frame(tabcontrol)

#adding tabs to tabcontrol, which adds them to the parent window root
tabcontrol.add(deviceConnectionTab, text = "Device Connection")
tabcontrol.add(testAndParametersTab, text = "Test and Parameters")
tabcontrol.add(dataAcquisitionTab, text = "Data Acquisition")

tabcontrol.pack(expand = 1, fill = "both")

#creating example labels inside the tabs
ttk.Label(deviceConnectionTab, text="DEVICE CONNECTION").grid(column = 1, row = 0)
ttk.Label(testAndParametersTab, text = "TEST AND PARAMETERS").grid(column = 0, row = 0, padx = 40, pady = 20)
ttk.Label(dataAcquisitionTab, text = "DATA ACQUISITION").grid(column = 0, row = 0)

##########TEST AND PARAMETERS TAB###############
TestAndParameters.addTestAndParameters(root, ttk, testAndParametersTab)
##########TEST AND PARAMETERS TAB###############

##########DATA ACQUISITION######################
ttk.Button(dataAcquisitionTab, text = "Graph!", command = graph.showgraph).grid(column = 0, row = 1, padx = 0, pady = 10)

root.mainloop()
