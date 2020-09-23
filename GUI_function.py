import GUI_design as at
import tkinter as tk
from tkinter import filedialog, Text
import os, sys, subprocess
import time

apps = []
loadFilename = '/home/jc/Resume_Projects/App_Opener_Advanced/save.txt'

def display_app_list(apps):
    print('in display app list')
    for app in apps:
        label = tk.Label(at.frame,text=app,bg="gray")
        label.pack()

def setscreen(loadFilename):
    print('in set screen')

    if loadFilename == '' or os.stat(loadFilename).st_size == 0 :
        print('Using default file')
        loadFilename = '/home/jc/Resume_Projects/App_Opener_Advanced/save.txt'
        
    else : 
        print('Using file : ',loadFilename)
        clearapps()
    
    with open(loadFilename,'r')as f:
        tempapps = f.read()
        tempapps = tempapps.split(',')
        if os.path.isfile(loadFilename):
            apps = [x for x in tempapps if x.strip()]
    
    display_app_list(apps)


#add apps to be opened
def addApp():
    print('in addApp')
    print(apps)
    for widget in at.frame.winfo_children(): 
        if widget != at.label1:
            widget.destroy()

    filename=filedialog.askopenfilename(initialdir="/",title="Select File")
    apps.append(filename)
    print(apps)
    display_app_list(apps)
    save_workspace()


#open the selected at.apps
def runapps():
    print('in run app')
    for app in apps:
        if sys.platform == "win32":
            os.startfile(app)
        else:
            opener ="open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, app])

def clearapps():
    print('in clear app')
    # if save.txt is not empty, create a copy of save.txt suffixed with mmddhhMM
    # else remove save.txt
    savefilename = '/home/jc/Resume_Projects/App_Opener_Advanced/save.txt'
    if os.path.isfile(savefilename):
        print('File Found',savefilename)
        if os.stat(savefilename).st_size !=0 :
            print('in if loop')
            ts1 = time.gmtime()
            ts1 = str(ts1.tm_mday)+str(ts1.tm_mon)+str(ts1.tm_hour)+str(ts1.tm_min)
            new_file_name = '/home/jc/Resume_Projects/App_Opener_Advanced/save'+ts1+'.txt'
            print(new_file_name)
            os.rename('/home/jc/Resume_Projects/App_Opener_Advanced/save.txt',new_file_name)
        else:
            print('in else loop')
            os.remove('/home/jc/Resume_Projects/App_Opener_Advanced/save.txt')

    #remove the commands from the screen 
    apps.clear()

    for widget in at.frame.winfo_children(): 
        if widget != at.label1:
            widget.destroy()

def save_workspace():
    print('in save workspace')
    with open('/home/jc/Resume_Projects/App_Opener_Advanced/save.txt','w') as f:
        for app in apps:
            f.write(app+',')

def saveFile():
    print('in save file')
    savefile = filedialog.asksaveasfilename(initialdir = "/home/jc/Resume_Projects/App_Opener_Advanced",title = "Save as",
    filetypes = (("text files","*.txt"),("all files","*.*")))

    with open(savefile,'w') as f:
        for app in apps:
            f.write(app+',')

def loadFile():
    print('in load file')
    loadFilename=filedialog.askopenfilename(initialdir = "/home/jc/Resume_Projects/App_Opener_Advanced",title = "Load_Workspace",
    filetypes = (("text files","*.txt"),("all files","*.*")))
    setscreen(loadFilename)



