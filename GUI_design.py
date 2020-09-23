import tkinter as tk
from PIL import ImageTk, Image
import GUI_function as BF
from tkinter import Menu,filedialog

root = tk.Tk()
root.title('Workspace Setter')

canvas = tk.Canvas(root, height=500, width=500, bg="white")
canvas.pack()
# canvas.place(relwidth=0.8,relheight=0.5,relx=0.1,rely=0.1)

#Set the background for canvas
def setbackground():
    print('in change bg')
    bk_image = filedialog.askopenfile(initialdir = "/home/jc/Resume_Projects/App_Opener_Advanced",title = "Choose Background Image",
    filetypes = (("image files","*.jpg"),("all files","*.*")))

    print(str(bk_image.name))

    if bk_image!='':
        bk_image = str(bk_image.name)
        img = ImageTk.PhotoImage(Image.open(bk_image).resize((500,500), Image.ANTIALIAS))
        canvas.background = img  # Keep a reference in case this code is put in a function.
        bg = canvas.create_image(0, 0, anchor=tk.NW, image=img)

#Create a Frame for displaying the app list
frame = tk.Frame(root)#,bg="skyblue",)
frame.place(relwidth=0.8,relheight=0.5,relx=0.1,rely=0.1)
label1 = tk.Label(frame,text="Your workspace :")
label1.pack()


menubar = Menu(root)

filemenu = Menu(menubar)
filemenu.add_command(label='Save Workspace', command = BF.saveFile)
filemenu.add_command(label='Load Workspace', command = BF.loadFile)
filemenu.add_command(label='Modify Default Location')
menubar.add_cascade(label="Workspace",menu=filemenu)

settings = Menu(menubar)
settings.add_command(label='Set Background',command = setbackground)
settings.add_command(label='Change default location')
menubar.add_cascade(label='Settings',menu=settings)

button_clearApps = tk.Button(root,text="Clear Set Apps",fg="black",bg="#f7cac9",command=BF.clearapps)
button_clearApps.pack(side=tk.LEFT,padx=5,pady=5)

button_runApps = tk.Button(root,text="Start my Workspace",fg="black",bg="#f7cac9",command=BF.runapps)
button_runApps.pack(side=tk.RIGHT,padx=5,pady=5)

button_openFile = tk.Button(root,text="Set my Workspace",fg="black",bg="#f7cac9",command=BF.addApp)
button_openFile.pack(side=tk.RIGHT)

root.config(menu=menubar)
root.mainloop()

