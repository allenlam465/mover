import os
import glob
import shutil
import errno
import tkinter

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

cwd = input("Input directory to be sorted: ")
fName = input("Input folder name that files will be placed in: ")

createFolder(cwd, fName)

dest = cwd + "/"+ fName

fType = input("What file type do you want to place into the folder: ")

getType(fType, dest)
