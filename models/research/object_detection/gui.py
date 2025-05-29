from tkinter import *
from tkinter import filedialog
from tkinter import Label
from tkinter import messagebox
import ShowResultFromModel as result

gui=Tk()
gui.minsize(640,420)
gui.title("OCR Deep Learning GUI")

def GetPictureName(event):
    
        filename=filedialog.askopenfile(initialdir="/",title="Select A File",filetype=(("jpeg","*.jpg"),("bitmap","*.bmp")))
        set_text(ImagePathName,filename.name)

    
def GetModelName(event):
    
    modelname=filedialog.askopenfile(initialdir="/",title="Select A File",)
    set_text(ModelPathName,modelname.name)
    

def StartModel():
    if ImagePathName.get()=="" or ModelPathName.get()=="":
        messagebox.showinfo("Warning", "No path image or model")
    
    else:    
        text=result.ShowResultFromModel(ImagePathName.get(),ModelPathName.get())
    

#set Text(ชื่อedittext,ข้อความ)
def set_text(EditTextID,text):
    EditTextID.delete(0,END)
    EditTextID.insert(0,text)
    return

btn_SelectImage=Button(text="Select Image:")
btn_SelectImage.bind('<Button-1>',GetPictureName)



btn_SelectModel=Button(text="Select Model:")
btn_SelectModel.bind('<Button-1>',GetModelName)


btn_Start=Button(text="Run Model",command=StartModel)

ImagePathLabel = Label(text="Select Image Path:")
ModelPathLabel=Label(text="Select Model Path:")


ImagePathName=Entry(bd=3)
ImagePathName.configure(state='normal')

ModelPathName=Entry(bd=3)
ModelPathName.configure(state='normal')

ImagePathLabel.grid(row=0,column=1,pady=50,padx=110)
ImagePathName.grid(row=1,column=1,pady=10)
btn_SelectImage.grid(row=2,column=1)

ModelPathLabel.grid(row=0,column=16)
ModelPathName.grid(row=1,column=16)
btn_SelectModel.grid(row=2,column=16)

btn_Start.grid(row=10,columnspan=32,padx=280,pady=100)


gui.mainloop()
