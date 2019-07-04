#!/usr/bin/env python3
#
#Application to move files from one directory to another.
#
#Run in terminal with :
#
#   python3 mover.py
#   /.mover.py
#

import os
import glob
import shutil
import errno

from tkinter import filedialog
from tkinter import messagebox
from sys import platform
from tkinter import *

class MainWindow(Frame):
    """Initilizes the class MainWindow for tkinter GUI.

        Args:
            master (str): Defines parent widget if any.
    """
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.__init__window()

    # Creates the window for user interaction.
    def __init__window(self):
        """Creates the GUI window based on grid system in tkinter."""
        self.master.title("Mover")
        self.pack(fill=BOTH, expand=1)

        # Get source and destination directory with file extension to move.
        Label(self, text="Source:").grid(row=0)
        Label(self, text="Destination:").grid(row=1)
        Label(self, text="Extension:").grid(row=2)

        # Allow user input or browse with button for source/destination location.
        self.entry1 = Entry(self)
        self.entry2 = Entry(self)
        self.entry3 = Entry(self)
        self.entry1.grid(row=0, column=1)
        self.entry2.grid(row=1, column=1)
        self.entry3.grid(row=2, column=1)

        #Buttons on GUI.
        browseButton = Button(self, text="Browse", command=self.loadSource)
        browseButton1 = Button(self, text="Browse", command=self.loadDest)
        applyButton = Button(self, text="Apply", command=self.moveFile)
        browseButton.grid(row=0, column=2, padx=5, pady=5)
        browseButton1.grid(row=1, column=2, padx=5, pady=5)
        applyButton.grid(row=3, column=1, padx=5, pady=5)

    def exit(self):
        """Exits program."""
        exit()

    def loadSource(self):
        """Loads source directory using tkinter filedialog."""
        cwd = filedialog.askdirectory()
        self.entry1.delete(0, END)
        self.entry1.insert(0, cwd)

    def loadDest(self):
        """Loads destination directory using tkinter filedialog."""
        dest = filedialog.askdirectory()
        self.entry2.delete(0, END)
        self.entry2.insert(0, dest)

    def moveFile(self):
        """Move files with the source and destination defined by user.
        
            Raises:
                shutilError: If file already exists in destination folder.
        """
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

    #New window to show all moved files.
    def listWindow(self, files):
        """Creates new window that lists all files moved.

        Args:
            files (:obj:`list` of :obj:`str`): List of all files moved.

        """
        list = '\n'.join(files)
        messagebox.showinfo("Moved Files", list)

    def errorWindow(self, text):
        """Creates new window that shows description of error.

        Args:
            text (str): Description of error occurance.

        """
        messagebox.showerror("Error", text)

    def owConfirm(self, text):
       """Window that appear to allow user to decide to overwrite an existing file.

        Args:
            text (str): File name.

        Returns:
            bool: Return value based on user choice. Yes for true. No for false.

        """
       return messagebox.askyesno("Overwrite File", text + "exist in destination directory. Overwrite?")

#Main
root = Tk()

if platform == 'darwin' or platform == 'linux':
    root.geometry("350x150")
elif platform == 'win32':
    root.geometry("250x130")

root.resizable(width=False, height=False)
app = MainWindow(root)
root.mainloop()
