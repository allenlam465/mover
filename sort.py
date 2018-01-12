import os
import glob
import shutil
import errno
from tkinter import *
from tkinter import filedialog

class Window(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master = master
        self.__init__window()

    def __init__window(self):
        self.master.title("Sorter")
        self.pack(fill=BOTH, expand=1)
        quitButton = Button(self,text="Quit", command=self.exit)
        quitButton.place(x=0,y=0)

    def exit(self):
        exit()

    def loadDir(self):
        dirName = askopenfilename(filetypes)

    def createFolder(cwd, fName):
        try:
            os.makedirs(cwd + "/" + fName)
        except OSError as e:
            if e.errno != errno.EEXIST:
                print("Folder exists.")
                raise

    def getType(type, path):
        for file in glob.glob(cwd + "/*." + type):
            print(file)
            shutil.move(file,path)

root = Tk()
root.geometry("600x300")
app = Window(root)
root.mainloop()

cwd = input("Input directory to be sorted: ")
fName = input("Input folder name that files will be placed in: ")

createFolder(cwd, fName)

dest = cwd + "/"+ fName

fType = input("What file type do you want to place into the folder: ")

getType(fType, dest)
