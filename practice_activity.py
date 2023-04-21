from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import os


root = Tk()
root.minsize(600,600)
root.maxsize(600,600)

open_img = ImageTk.PhotoImage(Image.open("opened-folder.png"))
save_img = ImageTk.PhotoImage(Image.open("save.png"))
exit_img = ImageTk.PhotoImage(Image.open("delete-sign.png"))

lf = Label(root,text="File name")
lf.place(relx=0.28,rely=0.03,anchor=CENTER)

ifn=Entry(root, text="File name")
ifn.place(relx=0.46, rely=0.03,anchor=CENTER)

my_text = Text(root,height=90, width=110)
my_text.place(relx=0.5,rely=0.55,anchor=CENTER)



name = ""
def openFile():
    my_text.delete(1.0, END)
    ifn.delete(0, END)
    text_file = filedialog.askopenfilename(title="open text file", filetype=(("Text Files", "*.txt"),))
    print(text_file)
    name = os.path.basename(text_file)
    formated_name = name.split('.')[0]
    ifn.insert(END,formated_name)
    root.title(formated_name)
    text_file = open(name,'r')
    
    paragraph=text_file.read()
    my_text.insert(END,paragraph)
    text_file.close()


def save():
    lf= ifn.get()
    file = open(lfe+".txt","w")
    data = my_text.get("1.0",END)
    print(data)
    file.write(data)
    ifn.delete(0, END)
    my_text.delete((1.0, END)
    messagebox.showinfo("Update","Success") 

def closeWindow():
    root.destroy()              

ob=Button(root,image=open_img, text="OpenFile", command=openFile)
ob.place(relx=0.05,rely=0.03,anchor=CENTER)

sb=Button(root, image=save_img, text="Save File", command=save)
sb.place(relx=0.11, rely=0.03,anchor=CENTER)

eb=Button(root, image=exit_img, text="Exit File", command=closeWindow)
eb.place(relx=0.17, rely=0.03,anchor=CENTER)

root.mainloop()





