import tkinter as tk
from tkinter import *
def addTestAndParameters(root, ttk, testAndParametersTab):
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
