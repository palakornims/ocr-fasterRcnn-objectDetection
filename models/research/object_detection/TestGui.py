from tkinter import *
from tkinter import filedialog
from tkinter import Label
from tkinter import messagebox
from tkinter import ttk
import ShowResultFromModel as result




class RunModelWindow:

    def __init__(self,master):
        self.master = master
        self.master.geometry('640x420')
        self.master.resizable(0,0)
        self.master.title("Run Model")
        self.frame =Frame(self.master)
        self.tab_control=ttk.Notebook(self.master)
        
        #tab control
        self.ModelRunTab=Frame(self.tab_control)
        self.ResultTab=Frame(self.tab_control)
        self.tab_control.add(self.ModelRunTab,text='Run Model')
        self.tab_control.add(self.ResultTab,text='Result')
        
        
       
        self.btn_SelectImage=Button(self.ModelRunTab,text="Select Image:")
        self.btn_SelectImage.bind('<Button-1>',self.GetPictureName)

        self.btn_SelectModel=Button(self.ModelRunTab,text="Select Model:")
        self.btn_SelectModel.bind('<Button-1>',self.GetModelName)

        self.btn_Start=Button(self.ModelRunTab,text="Run Model",command=self.StartModel)

        self.ImagePathLabel = Label(self.ModelRunTab,text="Select Image Path:")
        self.ModelPathLabel=Label(self.ModelRunTab,text="Select Model Path:")

        self.ImagePathName=Entry(self.ModelRunTab,bd=3)
        self.ImagePathName.configure(state='normal')
        
        self.ModelPathName=Entry(self.ModelRunTab,bd=3)
        self.ModelPathName.configure(state='normal')

        #component
        
        
        self.tab_control.pack(expand=1,fill='both')

        self.ImagePathLabel.grid(row=0,column=1,pady=50,padx=110)
        self.ImagePathName.grid(row=1,column=1,pady=10)
        

        self.ModelPathLabel.grid(row=0,column=16)
        self.ModelPathName.grid(row=1,column=16)
        self.btn_SelectModel.grid(row=2,column=16)
        self.btn_SelectImage.grid(row=2,column=1)
        self.btn_Start.grid(row=10,columnspan=32,padx=280,pady=100)
        
        #table in Result Tab
        self.ResultTable = ttk.Treeview(self.ResultTab)
        self.ResultTable['columns']=('OCR String','Result')
        self.ResultTable.heading('#0',text='Name',anchor='w')
        self.ResultTable.column("#0",anchor="w")
        self.ResultTable.heading('OCR String',text="OCR String")
        self.ResultTable.column('OCR String',anchor='center',width=220)
        self.ResultTable.heading('Result',text="Result")
        self.ResultTable.column('Result',anchor='center',width=220)
        self.ResultTable.grid(sticky=(N,S,W,E))
        self.treeview=self.ResultTable
        self.treeview.grid_rowconfigure(0, weight = 1)
        self.treeview.grid_columnconfigure(0, weight = 1)
        
        

    
    

    def GetPictureName(self,event):
    
            filename=filedialog.askopenfile(initialdir="/",title="Select A File",filetype=(("jpeg","*.jpg"),("bitmap","*.bmp")))
            self.set_text(self.ImagePathName,filename.name)
            
    def GetModelName(self,event):
    
            modelname=filedialog.askopenfile(initialdir="/",title="Select A File",filetype=[("PB File","*.pb")])
            self.set_text(self.ModelPathName,modelname.name)
     
    #เรียกไฟล์ทดสอบแบบจำลอง
    def StartModel(self):
            
            if self.ImagePathName.get()=="" or self.ModelPathName.get()=="":
                messagebox.showinfo("Warning", "No path image or model")
    
            else:    
                text=result.ShowResultFromModel(self.ImagePathName.get(),self.ModelPathName.get())
                self.InsertTable(text,self.GetPictureNameForLog(self.ImagePathName.get()))
                for child in self.treeview.get_children():

                    print(self.treeview.item(child)["text"])
                    print(self.treeview.item(child)["values"])

    def send(self):
        a=10
        return a
        

    #set Text(ชื่อedittext,ข้อความ)
    def set_text(self,EditTextID,text):
        EditTextID.delete(0,END)
        EditTextID.insert(0,text)
        return

    
   #Log ข้อมูลลง Table
    def InsertTable(self,string,ImagePath):
        self.treeview.insert('','end',text=ImagePath,values=(string[0],string[1]))

    def GetPictureNameForLog(self,ImagePathName):
        ImagePath = str(ImagePathName)
        ImageNameBeforeSort=""
        ImageNameAfterSort=""

        for Str in range(len(ImagePath),0,-1):
            if ImagePath[Str-1]=="/":
                break
            ImageNameBeforeSort=ImageNameBeforeSort+ImagePath[Str-1]
        for cat in range(len(ImageNameBeforeSort),0,-1):
            ImageNameAfterSort=ImageNameAfterSort+ImageNameBeforeSort[cat-1]

        return ImageNameAfterSort
        
def main():
    
    root=Tk()
    app=RunModelWindow(root)
    root.mainloop()

def main2():
    root=Tk()
    app=ResultModel(root)
    root.mainloop()

if __name__=='__main__':

    main()

        
