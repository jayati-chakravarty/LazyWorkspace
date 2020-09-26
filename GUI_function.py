import GUI_design as at
import tkinter as tk
from tkinter import filedialog, Text
import os, sys, subprocess
import time
from PIL import ImageTk, Image

apps = []
loadFilename = os.getcwd()+'/save.txt'
load_has_been_called = False

def fill_apps(loadfilename1):
    global apps
    with open(loadfilename1,'r')as f:
        tempapps = f.read()
        tempapps = tempapps.split(',')
        if os.path.isfile(loadfilename1):
            apps = [x for x in tempapps if x.strip()]


def display_app_list(apps):
    print('in display app list')
    for app in apps:
        label = tk.Label(at.frame,text=app,bg="gray")
        label.pack()

def setscreen(loadFilename1):
    print('in set screen')
    global apps
    global loadFilename

    if load_has_been_called == True:
        if loadFilename1 != '' or os.stat(loadFilename1).st_size > 0 :
            print('Using file : ',loadFilename1)
            loadFilename = loadFilename1
            for widget in at.frame.winfo_children(): 
                if widget not in(at.label1):
                    widget.destroy()
        
    else :
        print('Using default file',loadFilename)
        loadFilename = os.getcwd()+'/save.txt'
        if os.path.isfile(loadFilename) == False:
            with open(loadFilename, 'w') as f: 
                pass

    fill_apps(loadFilename)     
    print(apps)  
    
    display_app_list(apps)
    

#add apps to be opened
def addApp():
    print('in addApp')
    print(apps)
    for widget in at.frame.winfo_children(): 
        if widget != at.label1 :
            widget.destroy()

    filename=filedialog.askopenfilename(initialdir="/",title="Select File")
    apps.append(filename)
    print(apps)
    display_app_list(apps)
    save_workspace(loadFilename)


#open the selected at.apps
def runapps():
    print('in run app')
    for app in apps:
        if sys.platform == "win32":
            os.startfile(app)
        else:
            opener ="open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, app])

#Clear the workspace 
def clearapps():
    print('in clear app')
    if load_has_been_called == False:
        savefilename = os.getcwd()+'/save.txt'
        print(savefilename)
        if os.path.isfile(savefilename):
            print('File Found',savefilename)
            if os.stat(savefilename).st_size !=0 :
                print('in if loop')
                ts1 = time.gmtime()
                ts1 = str(ts1.tm_mday)+str(ts1.tm_mon)+str(ts1.tm_hour)+str(ts1.tm_min)
                new_file_name = os.getcwd()+'/save'+ts1+'.txt'
                print(new_file_name)
                os.rename(savefilename,new_file_name)
            else:
                print('in else loop')
                os.remove(savefilename)

    apps.clear()

    for widget in at.frame.winfo_children(): 
        if widget not in (at.label1) :
            widget.destroy()
 

def save_workspace(savefilename):
    print('in save workspace')
    print(savefilename)
    savefile_default = os.getcwd()+'/save.txt'

    if savefilename != '' and savefilename != savefile_default:
        if os.stat(savefilename).st_size > 0 :
            savefile_default = savefilename
            mode = 'a+'
    else :
        mode = 'w'
    
    with open(savefile_default,mode) as f:
        print('writing apps to',savefile_default)
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
    global load_has_been_called
    load_has_been_called = True
    print('in load file')
    loadFilename=filedialog.askopenfilename(initialdir = "/home/jc/Resume_Projects/App_Opener_Advanced",title = "Load_Workspace",
    filetypes = (("text files","*.txt"),("all files","*.*")))
    setscreen(loadFilename)

# setscreen(loadFilename)

