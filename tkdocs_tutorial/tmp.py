from Tkinter import *
from Tkinter import messagebox
from Tkinter import simpledialog
from Tkinter import filedialog

def ui_process():
    root =Tk()
    root.geometry("300x400+500+500")

#Tags   
    L_titile = Label(root,text='FHI',)
    L_titile.config(font='Helvetica -15 bold',fg='blue')
    L_titile.place(x=150,y=20,anchor="center")
    L_author = Label(root, text='Author:LCC')
    L_author.config(font='Helvetica -10 bold')
    L_author.place(x=250,y=380)

#Button
    B_0 = Button(root, text="dialog window", command=CreatDialog)
    B_0.place(x=90,y=200)
    B_1 = Button(root, text="Yes")#command=print)
    B_1.place(x=150, y=200)
    B_OK = Button(root,text="Create",command=lambda:button_process(root))
    B_OK.place(x=200,y=200)
    B_NO = Button(root, text="Cancel")
    B_NO.place(x=250,y=200)

#RadioButton
    v = IntVar()
    R_ONE=Radiobutton(root, text="One", variable=v, value=1,command=lambda:Print_b(1)).place(x=60,y=150)
    R_TWO=Radiobutton(root, text="Two", variable=v, value=2,command=lambda:Print_b(2)).place(x=10,y=150)

#Scrollbar
    W = Scale(root, from_=0, to=100,orient=HORIZONTAL)#orient=HORIZONTAL
    W.place(x=50,y=300)
    # print(W.get())  #get the scrollbar value

#Menu
    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Open", command=OpenFile)
    filemenu.add_command(label="Save", command=SaveFile)
    # filemenu.add_separator()#separator
    filemenu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=filemenu)
    root.config(menu=menubar)

    mainloop()

#Functions used in Buttons
def button_process(root):
    #create message box
    messagebox.askokcancel('Python Tkinter', 'Are you sure to create a window？')
    messagebox.askquestion('Python Tkinter', "Are you sure to create a window?")
    messagebox.askyesno('Python Tkinter', 'Are you sure to create a window？')
    messagebox.showerror('Python Tkinter', 'Unknown Error')
    messagebox.showinfo('Python Tkinter', 'hello world')
    messagebox.showwarning('Python Tkinter', 'Leave now')
    root1 = Toplevel(root)

def PrintHello():
    print("hello")

def Print_b(a):
    print(a)

#Create dialog
def CreatDialog():
    world = simpledialog.askstring('Python Tkinter', 'Input String', initialvalue = 'Python Tkinter')
    print(world)
    # simpledialog.askinteger()
    # simpledialog.askfloat()

#Dialog for file operator
def OpenFile():
    f = filedialog.askopenfilename(title='open file', filetypes=[('Python', '*.py *.pyw'), ('All Files', '*')])
    print(f)
    #could use os module to operate files
def SaveFile():
    f = filedialog.asksaveasfilename(title='save file', initialdir='/home/syang/syang/practices/python_GUI_Tkinter', initialfile='hello.py')
    print(f)
    #could use os module to save files
if __name__ == "__main__":
    print("Start")
    ui_process()
