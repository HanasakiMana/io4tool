import tkinter as tk
from tkinter import *
import os, sys
from IO import IO4
from const import *

class GUI(object):

    def __init__(self):
        self.window = Tk()
        self.window.title(appName)
        self.window.geometry(defaultSize) # size of window
        self.window.resizable(False, False)

        if getattr(sys, 'frozen', False): # whether is running in bundle
            base_path = sys._MEIPASS
        else:
            base_path = os.path.abspath(".")
        self.window.iconbitmap(os.path.join(base_path, 'favicon.ico'))

        self.inputFrame = Frame(self.window, width=600)
        self.outputFrame = Frame(self.window, width=600)
        self.inputFrame.pack(side='top', fill='x', ipadx=10, ipady=10, expand=0)
        self.outputFrame.pack(side='top', fill='both', ipadx=10, ipady=10, expand=1)

        self._initVaribles()

        self._initInputGrid()
        self._initOutputGrid()

        self.io = IO4()
        self.window.after(10, self._updateInputs)

    def _initVaribles(self):
        self.o1Val = BooleanVar()
        self.o2Val = BooleanVar()
        self.o3Val = BooleanVar()
        self.o4Val = BooleanVar()
        self.o5Val = BooleanVar()
        self.o6Val = BooleanVar()
        self.o7Val = BooleanVar()
        self.o8Val = BooleanVar()
        self.o9Val = BooleanVar()
        self.o10Val = BooleanVar()
        self.o11Val = BooleanVar()
        self.o12Val = BooleanVar()
        self.o13Val = BooleanVar()
        self.o14Val = BooleanVar()
        self.o15Val = BooleanVar()
        self.o16Val = BooleanVar()
        self.o17Val = BooleanVar()
        self.o18Val = BooleanVar()
        self.o19Val = BooleanVar()
        self.o20Val = BooleanVar()
        self.o21Val = BooleanVar()
        self.o22Val = BooleanVar()

        self.outputVar = [
            self.o1Val, self.o2Val, self.o3Val, self.o4Val, self.o5Val, 
            self.o6Val, self.o7Val, self.o8Val, self.o9Val, self.o10Val,
            self.o11Val, self.o12Val, self.o13Val, self.o14Val, self.o15Val,
            self.o16Val, self.o17Val, self.o18Val, self.o19Val, self.o20Val
        ]

    def _updateInputs(self):
        self.io.readReport()
        # digital inputs
        for i in range(len(inputs)):
            if self.io.buttons[inputs[i].byte] & (1 << inputs[i].shift):
                self.indicators[i].itemconfigure('indicator', fill='red')
            else:
                self.indicators[i].itemconfigure('indicator', fill='gray')
        # analog inputs
        for i in range(len(self.adcs)):
            self.adcs[i].configure(text=format(self.io.adcs[i*2] + (self.io.adcs[i*2+1] << 8), '04X'))
        self.window.after(8, self._updateInputs)
    
    def _updateOutput(self):
        for i in range(len(self.outputVar)):
            self.io.changeOutput(outputs[i], self.outputVar[i].get())
        self.io.sendReport()
    
    def _enableAllOutputs(self):
        for var in self.outputVar:
            var.set(1)
            self.io.changeAllOutputs(True)
            self.io.sendReport()
    
    def _disableAllOutputs(self):
        for var in self.outputVar:
            var.set(0)
            self.io.changeAllOutputs(False)
            self.io.sendReport()
    
    
    def _initInputGrid(self):

        frame = Frame(self.inputFrame)
        frame.pack(side='top')

        title = Label(frame, text='INPUT', font=("Arial", 20), pady=10)
        title.grid(row=0, column=2)
        
        # 1P
        title = Label(frame, text='1P', font=("Arial", 15), width=6)
        title.grid(row=1, column=0)

        self.i1 = self._createInputIndicator(frame, 1, 1, 'START')
        self.i25 = self._createInputIndicator(frame, 1, 2, 'SERVICE')
        self.i3 = self._createInputIndicator(frame, 2, 1, 'RIGHT')
        self.i5 = self._createInputIndicator(frame, 2, 2, 'LEFT')
        self.i7 = self._createInputIndicator(frame, 2, 3, 'UP')
        self.i9 = self._createInputIndicator(frame, 2, 4, 'DOWN')
        self.i11 = self._createInputIndicator(frame, 3, 1, 'PUSH 1')
        self.i13 = self._createInputIndicator(frame, 3, 2, 'PUSH 2')
        self.i15 = self._createInputIndicator(frame, 3, 3, 'PUSH 3')
        self.i17 = self._createInputIndicator(frame, 3, 4, 'PUSH 4')
        self.i19 = self._createInputIndicator(frame, 4, 1, 'PUSH 5')
        self.i21 = self._createInputIndicator(frame, 4, 2, 'PUSH 6')
        self.i23 = self._createInputIndicator(frame, 4, 3, 'PUSH 7')
        self.i31 = self._createInputIndicator(frame, 4, 4, 'PUSH 8')

        # 2P
        title = Label(frame, text='2P', font=("Arial", 15), width=6)
        title.grid(row=5, column=0)

        self.i2 = self._createInputIndicator(frame, 5, 1, 'START')
        self.i26 = self._createInputIndicator(frame, 5, 2, 'SERVICE')
        self.i4 = self._createInputIndicator(frame, 6, 1, 'RIGHT')
        self.i6 = self._createInputIndicator(frame, 6, 2, 'LEFT')
        self.i8 = self._createInputIndicator(frame, 6, 3, 'UP')
        self.i10 = self._createInputIndicator(frame, 6, 4, 'DOWN')
        self.i12 = self._createInputIndicator(frame, 7, 1, 'PUSH 1')
        self.i14 = self._createInputIndicator(frame, 7, 2, 'PUSH 2')
        self.i16 = self._createInputIndicator(frame, 7, 3, 'PUSH 3')
        self.i18 = self._createInputIndicator(frame, 7, 4, 'PUSH 4')
        self.i20 = self._createInputIndicator(frame, 8, 1, 'PUSH 5')
        self.i22 = self._createInputIndicator(frame, 8, 2, 'PUSH 6')
        self.i24 = self._createInputIndicator(frame, 8, 3, 'PUSH 7')
        self.i32 = self._createInputIndicator(frame, 8, 4, 'PUSH 8')

        # System
        title = Label(frame, text='System', font=("Arial", 15), width=6)
        title.grid(row=9, column=0)

        self.i27 = self._createInputIndicator(frame, 9, 1, 'TEST')
        self.i28 = self._createInputIndicator(frame, 9, 2, 'TILT')
        self.i29 = self._createInputIndicator(frame, 9, 3, 'COIN 1')
        self.i30 = self._createInputIndicator(frame, 9, 4, 'COIN 2')

        # create a array for all digital inputs
        self.indicators = [
            self.i1, self.i2, self.i3, self.i4, self.i5, self.i6, self.i7, self.i8,
            self.i9, self.i10, self.i11, self.i12, self.i13, self.i14, self.i15, self.i16,
            self.i17, self.i18, self.i19, self.i20, self.i21, self.i22, self.i23, self.i24,
            self.i25, self.i26, self.i27, self.i28, self.i29, self.i30, self.i31, self.i32
        ]

        # ADCs
        title = Label(frame, text='ADCs', font=("Arial", 15), width=6)
        title.grid(row=10, column=0)

        self.adc1 = Label(frame, text='', font=("Arial", 15))
        self.adc1.grid(row=10, column=1)
        self.adc2 = Label(frame, text='', font=("Arial", 15))
        self.adc2.grid(row=10, column=2)
        self.adc3 = Label(frame, text='', font=("Arial", 15))
        self.adc3.grid(row=10, column=3)
        self.adc4 = Label(frame, text='', font=("Arial", 15))
        self.adc4.grid(row=10, column=4)
        self.adc5 = Label(frame, text='', font=("Arial", 15))
        self.adc5.grid(row=11, column=1)
        self.adc6 = Label(frame, text='', font=("Arial", 15))
        self.adc6.grid(row=11, column=2)
        self.adc7 = Label(frame, text='', font=("Arial", 15))
        self.adc7.grid(row=11, column=3)
        self.adc8 = Label(frame, text='', font=("Arial", 15))
        self.adc8.grid(row=11, column=4)

        self.adcs = [
            self.adc1, self.adc2, self.adc3, self.adc4,
            self.adc5, self.adc6, self.adc7, self.adc8
        ]      

    def _createInputIndicator(self, frame: Frame, row: int, column: int, text: str):
        group = Frame(frame)
        indicator = Canvas(group, width=25, height=25)
        indicator.pack(side='left')
        indicator.create_oval(5, 5, 25, 25, fill='red', tags=('indicator'))
        text = Label(group, text=text, font=("Arial", 15), width=10)
        text.pack(side='right')
        group.grid(row=row, column=column)
        return indicator
    
    def _initOutputGrid(self):
        frame = Frame(self.outputFrame)
        frame.pack(side='top')
        
        title = Label(frame, text='OUTPUT', font=("Arial", 20))
        title.grid(row=0, column=2)

        btnO1 = Checkbutton(frame, text='Output 01', variable=self.o1Val, onvalue=True, offvalue=False, command=self._updateOutput, font=("Arial", 15), width=10)
        btnO1.grid(row=1, column=0)
        btnO2 = Checkbutton(frame, text='Output 02', variable=self.o2Val, onvalue=True, offvalue=False, command=self._updateOutput, font=("Arial", 15), width=10)
        btnO2.grid(row=1, column=1)
        btnO3 = Checkbutton(frame, text='Output 03', variable=self.o3Val, onvalue=True, offvalue=False, command=self._updateOutput, font=("Arial", 15), width=10)
        btnO3.grid(row=1, column=2)
        btnO4 = Checkbutton(frame, text='Output 04', variable=self.o4Val, onvalue=True, offvalue=False, command=self._updateOutput, font=("Arial", 15), width=10)
        btnO4.grid(row=1, column=3)
        btnO5 = Checkbutton(frame, text='Output 05', variable=self.o5Val, onvalue=True, offvalue=False, command=self._updateOutput, font=("Arial", 15), width=10)
        btnO5.grid(row=1, column=4)
        btnO6 = Checkbutton(frame, text='Output 06', variable=self.o6Val, onvalue=True, offvalue=False, command=self._updateOutput, font=("Arial", 15), width=10)
        btnO6.grid(row=2, column=0)
        btnO7 = Checkbutton(frame, text='Output 07', variable=self.o7Val, onvalue=True, offvalue=False, command=self._updateOutput, font=("Arial", 15), width=10)
        btnO7.grid(row=2, column=1)
        btnO8 = Checkbutton(frame, text='Output 08', variable=self.o8Val, onvalue=True, offvalue=False, command=self._updateOutput, font=("Arial", 15), width=10)
        btnO8.grid(row=2, column=2)
        btnO9 = Checkbutton(frame, text='Output 09', variable=self.o9Val, onvalue=True, offvalue=False, command=self._updateOutput, font=("Arial", 15), width=10)
        btnO9.grid(row=2, column=3)
        btnO10 = Checkbutton(frame, text='Output 10', variable=self.o10Val, onvalue=True, offvalue=False, command=self._updateOutput, font=("Arial", 15), width=10)
        btnO10.grid(row=2, column=4)
        btnO11 = Checkbutton(frame, text='Output 11', variable=self.o11Val, onvalue=True, offvalue=False, command=self._updateOutput, font=("Arial", 15), width=10)
        btnO11.grid(row=3, column=0)
        btnO12 = Checkbutton(frame, text='Output 12', variable=self.o12Val, onvalue=True, offvalue=False, command=self._updateOutput, font=("Arial", 15), width=10)
        btnO12.grid(row=3, column=1)
        btnO13 = Checkbutton(frame, text='Output 13', variable=self.o13Val, onvalue=True, offvalue=False, command=self._updateOutput, font=("Arial", 15), width=10)
        btnO13.grid(row=3, column=2)
        btnO14 = Checkbutton(frame, text='Output 14', variable=self.o14Val, onvalue=True, offvalue=False, command=self._updateOutput, font=("Arial", 15), width=10)
        btnO14.grid(row=3, column=3)
        btnO15 = Checkbutton(frame, text='Output 15', variable=self.o15Val, onvalue=True, offvalue=False, command=self._updateOutput, font=("Arial", 15), width=10)
        btnO15.grid(row=3, column=4)
        btnO16 = Checkbutton(frame, text='Output 16', variable=self.o16Val, onvalue=True, offvalue=False, command=self._updateOutput, font=("Arial", 15), width=10)
        btnO16.grid(row=4, column=0)
        btnO17 = Checkbutton(frame, text='Output 17', variable=self.o17Val, onvalue=True, offvalue=False, command=self._updateOutput, font=("Arial", 15), width=10)
        btnO17.grid(row=4, column=1)
        btnO18 = Checkbutton(frame, text='Output 18', variable=self.o18Val, onvalue=True, offvalue=False, command=self._updateOutput, font=("Arial", 15), width=10)
        btnO18.grid(row=4, column=2)
        btnO19 = Checkbutton(frame, text='Output 19', variable=self.o19Val, onvalue=True, offvalue=False, command=self._updateOutput, font=("Arial", 15), width=10)
        btnO19.grid(row=4, column=3)
        btnO20 = Checkbutton(frame, text='Output 20', variable=self.o20Val, onvalue=True, offvalue=False, command=self._updateOutput, font=("Arial", 15), width=10)
        btnO20.grid(row=4, column=4)

        btn21 = Button(frame, text='Select All', command=self._enableAllOutputs, font=("Arial", 15), width=10)
        btn21.grid(row=5, column=1, pady=10)
        btn22 = Button(frame, text='Deselect All', command=self._disableAllOutputs, font=("Arial", 15), width=10)
        btn22.grid(row=5, column=3, pady=10)
    
    def start(self):
        self.window.mainloop()
