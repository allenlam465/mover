#!/usr/bin/env python3
# mover.py - Application to move files from one directory to another.

import os
import glob
import shutil
import errno
from tkinter import filedialog
from tkinter import messagebox
from tkinter import *


class MainWindow(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.__init__window()

    # Creates window for user interaction.
    def __init__window(self):
        self.master.title("Mover")
        self.pack(fill=BOTH, expand=1)

        # Get source and destination directory with file extension to move.
        Label(self, text="Source:").grid(row=0)
        Label(self, text="Destination:").grid(row=1)
        Label(self, text="Extension:").grid(row=2)

        # Allow user input or browse with button.
        self.entry1 = Entry(self)
        self.entry2 = Entry(self)
        self.entry3 = Entry(self)
        self.entry1.grid(row=0, column=1)
        self.entry2.grid(row=1, column=1)
        self.entry3.grid(row=2, column=1)

        browseButton = Button(self, text="Browse", command=self.loadSource)
        browseButton1 = Button(self, text="Browse", command=self.loadDest)
        applyButton = Button(self, text="Apply", command=self.moveFile)
        quitButton = Button(self, text="Quit", command=self.exit)
        browseButton.grid(row=0, column=2)
        browseButton1.grid(row=1, column=2)
        applyButton.grid(row=3, column=1)
        quitButton.grid(row=4, column=1)

    def exit(self):
        exit()

    def loadSource(self):
        cwd = filedialog.askdirectory()
        self.entry1.delete(0, END)
        self.entry1.insert(0, cwd)

    def loadDest(self):
        dest = filedialog.askdirectory()
        self.entry2.delete(0, END)
        self.entry2.insert(0, dest)

    def moveFile(self):
        expression = self.entry3.get()
        file_list = []

        # Catch exceptions if shutil has errors.
        try:
            for ext in expression.split(","):
                for file in glob.glob(self.entry1.get() + "/*." + ext):
                    file_list.append(file)
                    file_name = os.path.basename(file)
                    if(os.path.exists(self.entry2.get() + "/" + file_name)):
                        results = self.owConfirm(file_name)
                        if(results):
                            shutil.copy(file, self.entry2.get())
                            os.remove(file)
                    else:
                        shutil.move(file, self.entry2.get())
        except shutil.Error as err:
            self.errorWindow(err)
            pass

        self.listWindow(file_list)

    def listWindow(self, files):
        list = '\n'.join(files)
        messagebox.showinfo("Moved Files", list)

    def errorWindow(self, text):
        messagebox.showerror("Error", text)

    def owConfirm(self, text):
        return messagebox.askyesno("Overwrite File", text +
                                   "exist in destination directory. Overwrite?")


root = Tk()
root.geometry("350x150")
app = MainWindow(root)
root.mainloop()
