import tkinter as tk
from tkinter import *

def addTestAndParameters(root, ttk, testAndParametersTab):
    def clear_screen():
        for widgets in testAndParametersTab.winfo_children():
            if(str(widgets) =='.!notebook.!frame2.!label' or str(widgets) =='.!notebook.!frame2.!label2' or str(widgets) =='.!notebook.!frame2.!optionmenu'):
                continue
            else:
                widgets.destroy()

    def display_selected(choice):
        choice = voltametricTestValue.get()
        if(choice == 'constant voltage'):
            clear_screen()
            # current range uA
            currentRangeValue = StringVar(root)
            ttk.Label(testAndParametersTab, text='Current Range uA', anchor='w').grid(column=0, row=3)
            ttk.OptionMenu(testAndParametersTab, currentRangeValue, 'select', '1', '10', '100', '1000').grid(column=0,row=4,padx=10,pady=20)

            # Sample rate (Hz)
            sampleRateValue = StringVar(root)
            ttk.Label(testAndParametersTab, text='Sample Rate (Hz)', anchor='w').grid(column=0, row=5)
            ttk.Spinbox(testAndParametersTab, textvariable=sampleRateValue, from_=0, to=200).grid(column=0, row=6,padx=10, pady=20)

            # quiet time(s)
            quietTimeValue = StringVar(root)
            ttk.Label(testAndParametersTab, text='Quiet time (s)', anchor='w').grid(column=0, row=7)
            tk.Spinbox(testAndParametersTab, textvariable = quietTimeValue).grid(column=0, row=8, padx=10, pady=20)

            # quiet value (V)
            quietValue = StringVar(root)
            ttk.Label(testAndParametersTab, text='Quiet value (V)', anchor='w').grid(column=0, row=9)
            tk.Spinbox(testAndParametersTab, textvariable = quietValue).grid(column=0, row=10, padx=10, pady=20)

            # value (V)
            valueValue = StringVar(root)
            ttk.Label(testAndParametersTab, text='Value (V)', anchor='w').grid(column=0, row=11)
            tk.Spinbox(testAndParametersTab, textvariable = valueValue).grid(column=0, row=12, padx=10, pady=20)

            # duration
            durationValue = StringVar(root)
            ttk.Label(testAndParametersTab, text='Duration (s)', anchor='w').grid(column=0, row=13)
            tk.Spinbox(testAndParametersTab, textvariable = durationValue).grid(column=0, row=14, padx=10, pady=20)

        elif (choice == 'chronoamperometry'):
            clear_screen()
            # current range uA
            currentRangeValue = StringVar(root)
            ttk.Label(testAndParametersTab, text='Current Range uA', anchor='w').grid(column=0, row=3)
            ttk.OptionMenu(testAndParametersTab, currentRangeValue, 'select', '1', '10', '100', '1000').grid(column=0,row=4,padx=10,pady=20)

            # Sample rate (Hz)
            sampleRateValue = StringVar(root)
            ttk.Label(testAndParametersTab, text='Sample Rate (Hz)', anchor='w').grid(column=0, row=5)
            ttk.Spinbox(testAndParametersTab, textvariable=sampleRateValue, from_=0, to=200).grid(column=0, row=6,
                                                                                                  padx=10, pady=20)

            # quiet time(s)
            quietTimeValue = StringVar(root)
            ttk.Label(testAndParametersTab, text='Quiet time (s)', anchor='w').grid(column=0, row=7)
            tk.Spinbox(testAndParametersTab, textvariable = quietTimeValue).grid(column=0, row=8, padx=10, pady=20)

            # quiet value(V)
            quietValue = StringVar(root)
            ttk.Label(testAndParametersTab, text='Quiet value (s)', anchor='w').grid(column=0, row=9)
            tk.Spinbox(testAndParametersTab, textvariable = quietValue).grid(column=0, row=10, padx=10, pady=20)

            # step 1 duration(s)  
            step1DurationTimeValue = StringVar(root)
            ttk.Label(testAndParametersTab, text='Step 1 duration (s)', anchor='w').grid(column=0, row=11)
            tk.Spinbox(testAndParametersTab, textvariable = step1DurationTimeValue).grid(column=0, row=12, padx=10, pady=20)

            # step 1 value(V)  
            step1DurationValue = StringVar(root)
            ttk.Label(testAndParametersTab, text='Step 1 value (V)', anchor='w').grid(column=0, row=13)
            tk.Spinbox(testAndParametersTab, textvariable = step1DurationValue).grid(column=0, row=14, padx=10, pady=20)

            # step 2 duration(s)  
            step2DurationTimeValue = StringVar(root)
            ttk.Label(testAndParametersTab, text='Step 2 duration (s)', anchor='w').grid(column=0, row=15)
            tk.Spinbox(testAndParametersTab, textvariable = step2DurationTimeValue).grid(column=0, row=16, padx=10, pady=20)

            # step 1 value(V)  
            step2DurationValue = StringVar(root)
            ttk.Label(testAndParametersTab, text='Step 2 value (V)', anchor='w').grid(column=0, row=17)
            tk.Spinbox(testAndParametersTab, textvariable = step2DurationValue).grid(column=0, row=18, padx=10, pady=20)

        else:
            pass

#voltametric test
    voltametricTestValue = StringVar(root)
    ttk.Label(testAndParametersTab, text = 'Voltametric Test', anchor = 'w').grid(column = 0, row = 1)
    ttk.OptionMenu(testAndParametersTab, voltametricTestValue, 'select','constant voltage', 'chronoamperometry', 'cyclic', 'linear sweep', 'sinusoid',command=display_selected).grid(column = 0, row = 2, padx = 10, pady = 20)
