#!/usr/bin/env python
#sort.py - Application to move files from one directory to another. 

import os
import glob
import shutil
import errno
from tkinter import filedialog
from tkinter import *

class Window(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master = master
        self.__init__window()

    def __init__window(self):
        self.master.title("Sorter")
        self.pack(fill=BOTH, expand=1)
        Label(self, text="Source:").grid(row=0)
        Label(self, text="Destination:").grid(row=1)
        Label(self, text="Extension:").grid(row=2)

        self.entry1 = Entry(self)
        self.entry2 = Entry(self)
        self.entry3 = Entry(self)
        self.entry1.grid(row=0,column=1)
        self.entry2.grid(row=1,column=1)
        self.entry3.grid(row=2,column=1)

        browseButton = Button(self, text="Browse", command= self.loadSource)
        browseButton1 = Button(self, text="Browse", command= self.loadDest)
        applyButton = Button(self, text="Apply", command= self.moveFile)
        quitButton = Button(self, text="Quit", command=self.exit)
        browseButton.grid(row=0, column=2)
        browseButton1.grid(row=1, column=2)
        applyButton.grid(row=3,column=1)
        quitButton.grid(row=4,column=1)

    def exit(self):
        exit()

    def loadSource(self):
        cwd = filedialog.askdirectory()
        self.entry1.delete(0,END)
        self.entry1.insert(0,cwd)

    def loadDest(self):
        dest = filedialog.askdirectory()
        self.entry2.delete(0,END)
        self.entry2.insert(0,dest)

    def moveFile(self):
        for file in glob.glob(self.entry1.get() + "/*." + self.entry3.get()):
            print(file)
            shutil.move(file,self.entry2.get())

root = Tk()
root.geometry("350x150")
app = Window(root)
root.mainloop()
