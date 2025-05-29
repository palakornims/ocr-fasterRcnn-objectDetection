from tkinter import *
from tkinter import filedialog
from tkinter import Label
import ShowResultFromModel as result
gui=Tk()
gui.minsize(640,400)

def fOpen(event):
    filename=filedialog.askopenfile(initialdir="/",title="Select A File",filetype=(("jpeg","*.jpg"),("bitmap","*.bmp")))
    label1=Label(text=filename.name).pack()
    return label1
    
def ModelOpen(event):
    modelname=filedialog.askopenfile(initialdir="/",title="Select A File",)
    label=Label(text=modelname.name).pack()
    return label

def StartModel(event):
    text=result.ShowResultFromModel(fOpen(),ModelOpen())

b1=Button(text="Select File:")
b1.bind('<Button-1>',fOpen)
b1.pack()


b2=Button(text="Select model:")
b2.bind('<Button-1>',ModelOpen)
b2.pack()

b3=Button(text="Start:")
b3.bind('<Button-1>',StartModel)
b3.pack()


gui.mainloop()
