from pyqtgraph.Qt import QtGui, QtCore
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
from collections import deque
import sys  # We need sys so that we can pass argv to QApplication
import os
from random import randint



class CustomPeripheral:
    def __init__(self, name):
        self.NAME = name
        self.ADDR = "unknown"
        self.SYSCFG = "f000abcd-0451-4000-b000-000000000000"
        self.CHAR1 = "f00062d2-0451-4000-b000-000000000000"
        self.CHAR2 = "f00044dc-0451-4000-b000-000000000000"
        self.CHAR3 = "f0003c36-0451-4000-b000-000000000000"
        self.CHAR4 = "f0003a36-0451-4000-b000-000000000000"
        self.CHAR5 = "f00030d8-0451-4000-b000-000000000000"
        self.CHAR1_DATA =[]
        self.CHAR2_DATA =[]
        self.CHAR3_DATA =[]
        self.CHAR4_DATA =[]
        self.CHAR5_DATA =[]
        self.datacount = 0


    def get_address(self,device_list):
        for device in device_list:
            if device.name == self.NAME:
                self.ADDR = device.address
                return True
        return False

    def parse_data(self, sender,data):
        if sender == self.CHAR1:
            self.CHAR1_DATA.append(int(data[0]))
            return 1
        if sender == self.CHAR2:
            self.CHAR2_DATA.append(int(data[0]))
            return 2
        if sender == self.CHAR3:
            self.CHAR3_DATA.append(int(data[0]))
            return 3
        if sender == self.CHAR4:
            self.CHAR4_DATA.append(int(data[0]))
            return 4
        if sender == self.CHAR5:
            self.CHAR5_DATA.append(int(data[0]))
            return 5


class CPPlot:
    def __init__(self,app,win,win_size):
        self.win_size = win_size
        # self.p1_data = deque([0]*self.win_size)
        # self.p2_data = deque([0]*self.win_size)
        # self.p3_data = deque([0]*self.win_size)
        # self.p4_data = deque([0]*self.win_size)
        # self.p5_data = deque([0]*self.win_size)
        self.plot_data = [deque([0]*self.win_size) for i in range(5)]

        self.app = app
        self.win = win
        self.char1_plot = win.addPlot(row=1, col=1, colspan=5, title="Char 1")
        self.char2_plot = win.addPlot(row=2, col=1, colspan=5, title="Char 2")
        self.char3_plot = win.addPlot(row=3, col=1, colspan=5, title="Char 3")
        self.char4_plot = win.addPlot(row=4, col=1, colspan=5, title="Char 4")
        self.char5_plot = win.addPlot(row=5, col=1, colspan=5, title="Char 5")
        self.char_plots = [self.char1_plot,self.char2_plot, self.char3_plot,self.char4_plot,self.char5_plot]

    def plot_char(self, char_num, data):
        char_ind = char_num - 1
        self.plot_data[char_ind].append(data)
        self.plot_data[char_ind].popleft()
        self.char_plots[char_ind].plot(self.plot_data[char_ind], clear= True)

    def update(self):
        pg.QtGui.QApplication.processEvents()



