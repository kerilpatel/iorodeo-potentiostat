import tkinter as tk
from tkinter import *
from tkinter import ttk
import matplotlib.pyplot as plt

#creating parent window
root = tk.Tk()
root.title("IORODEO POTENTIOSTAT")
root.geometry("1280x720")

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
#voltametric test
voltametricTestValue = StringVar(root)
ttk.Label(testAndParametersTab, text = 'Voltametric Test', anchor = 'w').grid(column = 0, row = 1)
ttk.OptionMenu(testAndParametersTab, voltametricTestValue, 'select','constant voltage', 'chronoamperometry', 'cyclic', 'linear sweep', 'sinusoid').grid(column = 0, row = 2, padx = 10, pady = 20)

#current range uA
currentRangeValue = StringVar(root)
ttk.Label(testAndParametersTab, text = 'Current Range uA', anchor = 'w').grid(column = 0, row = 3)
ttk.OptionMenu(testAndParametersTab, currentRangeValue, 'select','1', '10', '100', '1000').grid(column = 0, row = 4, padx = 10, pady = 20)

#Sample rate (Hz)
sampleRateValue = StringVar(root)
ttk.Label(testAndParametersTab, text = 'Sample Rate (Hz)', anchor = 'w').grid(column = 0, row = 5)
ttk.Spinbox(testAndParametersTab,  textvariable = sampleRateValue, from_ = 0, to = 200).grid(column = 0, row = 6, padx = 10, pady = 20)

#quiet time(s)
ttk.Label(testAndParametersTab, text = 'Quiet time (s)', anchor = 'w').grid(column = 0, row = 7)
tk.Text(testAndParametersTab, height = 1, width = 10).grid(column = 0, row = 8, padx = 10, pady = 20)

#quiet value (V)
ttk.Label(testAndParametersTab, text = 'Quiet value (V)', anchor = 'w').grid(column = 0, row = 9)
tk.Text(testAndParametersTab, height = 1, width = 10).grid(column = 0, row = 10, padx = 10, pady = 20)

#value (V)
ttk.Label(testAndParametersTab, text = 'Value (V)', anchor = 'w').grid(column = 0, row = 11)
tk.Text(testAndParametersTab, height = 1, width = 10).grid(column = 0, row = 12, padx = 10, pady = 20)

#duration
ttk.Label(testAndParametersTab, text = 'Duration (s)', anchor = 'w').grid(column = 0, row = 13)
tk.Text(testAndParametersTab, height = 1, width = 10).grid(column = 0, row = 14, padx = 10, pady = 20)

##########TEST AND PARAMETERS TAB###############

##########DATA ACQUISITION######################

def showgraph():

    potential = [10, 12, 17, 26, 50]
    time = [2, 4, 6, 8, 10]

    fig, axs = plt.subplots()

    axs.plot(potential, time)
    axs.set(xlabel = 'time', ylabel = 'potential')
    axs.grid()
    plt.show()

ttk.Button(dataAcquisitionTab, text = "Graph!", command = showgraph).grid(column = 0, row = 1, padx = 0, pady = 10)






root.mainloop()












