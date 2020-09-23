import tkinter as tk
from PIL import ImageTk, Image
import GUI_function as BF

root = tk.Tk()
root.title('Workspace Setter')

canvas = tk.Canvas(root, height=500, width=500, bg="white")
canvas.pack()

#Set the background for canvas
bk_image = '/home/jc/Resume_Projects/App_Opener_Advanced/bg-image.jpg'
img = ImageTk.PhotoImage(Image.open(bk_image).resize((500,500), Image.ANTIALIAS))
canvas.background = img  # Keep a reference in case this code is put in a function.
bg = canvas.create_image(0, 0, anchor=tk.NW, image=img)

frame = tk.Frame(root,bg="skyblue",)
frame.place(relwidth=0.8,relheight=0.5,relx=0.1,rely=0.1)
label1 = tk.Label(frame,text="Your workspace :")
label1.pack()

button_clearApps = tk.Button(root,text="Clear Set Apps",fg="black",bg="#f7cac9",command=BF.clearapps)
button_clearApps.pack(side=tk.LEFT,padx=5,pady=5)

button_runApps = tk.Button(root,text="Start my Workspace",fg="black",bg="#f7cac9",command=BF.runapps)
button_runApps.pack(side=tk.RIGHT,padx=5,pady=5)

button_openFile = tk.Button(root,text="Set my Workspace",fg="black",bg="#f7cac9",command=BF.addApp)
button_openFile.pack(side=tk.RIGHT)

button_saveFile = tk.Button(root,text="Save my Workspace",fg="black",bg="#f7cac9",command=BF.saveFile)
button_saveFile.pack(side=tk.LEFT)

button_loadFile = tk.Button(root,text="Load my Workspace",fg="black",bg="#f7cac9",command=BF.loadFile)
button_loadFile.pack(side=tk.LEFT)

root.mainloop()

