from Tkinter import *
import ttk
import tkFileDialog
import tkMessageBox

###root window
root =Tk()
root.configure(bg='lightgrey')
root.title('Select the files to upload')
#root.geometry('680x400')

lbl1 = Label(root, text='file list', font=('Helvetica', 16, 'bold'))
lbl1.grid(row=0, column=0, sticky=W)

#funtions:open a filedialog window,select files and add it to the listbox

uploadfilename_dict = {}
msg = StringVar()
def file_directory_get(*args):
    file_directory = tkFileDialog.askopenfilename(initialdir = '/home/syang', title='Select file', \
                                                  filetypes = (("zip files","*.zip"),("tar files","*.tar.gz"),("all files","*.*")))
    try:
        uploadfilename_dict[file_directory.split('/')[-1]]
    except KeyError:
        uploadfilename_dict[file_directory.split('/')[-1]] = file_directory #file_directory.split('/')[-1] is the file name
        listfile.insert(END, file_directory.split('/')[-1])
    else:
        tkMessageBox.showinfo("Warning", "File already exists in the list!")#Add a existing file would accept a warning

def remove_selected_listitem(): ##to be checked
    current_selection = listfile.curselection()
    idx = int(current_selection[0])
    msg.set('File \' %s \' has been deleted from the upload list!' % listfile.get(idx))
    
    del uploadfilename_dict[listfile.get(int(idx))] #delete it also in the dict
    listfile.delete(current_selection)
    


#frame1:filelist and scrollbar
frm1 = Frame(root)#padding=(5, 5, 12, 0))
frm1.grid(row=1, column=0, sticky=(N,S))
root.rowconfigure(1, weight=1)
root.columnconfigure(1, weight=1)

scrollbar = Scrollbar(frm1, orient=VERTICAL)
scrollbar.pack(side=RIGHT, fill=Y)


#fnames=StringVar(value=selectedfilenames)
listfile = Listbox(frm1, width=20, yscrollcommand=scrollbar.set, font=('Helvetica', 12))
listfile.pack(expand=True, fill=Y)

scrollbar.config(command=listfile.yview)

#frame2:buttons
#frm2 = Frame(root)
#frm2.grid(row=1, column=1, sticky=(N,S,E,W))
#root.rowconfigure(2, weight=1)
#root.columnconfigure(2, weight=1)
#prsent not use frame2
#Buttons
add_button = Button(root, text='Add',command=file_directory_get, font=('Helvetica', 8), width=6, height=1)
remove_button = Button(root, text='Remove',command=remove_selected_listitem, font=('Helvetica', 8), width=6, height=1)
upload_button = Button(root, text='Upload',font=('Helvetica', 8), width=6, height=1)#command=??
exit_button = Button(root, text='Cancel', command=root.quit, font=('Helvetica', 8), width=6, height=1)
msg_label = Label(root, textvariable=msg, anchor='center')

add_button.grid(row=0, column=1, padx=5)
remove_button.grid(row=1, column=1, padx=5, pady=2)
msg_label.grid(row=2, column=1, padx=5, pady=2)
upload_button.grid(row=3, column=1, padx=5, pady=6)
exit_button.grid(row=4, column=1, padx=5, pady=6)

#for x in range(100):
#    tmp = 'filename' + str(x)
#    listfile.insert(END, tmp)


root.mainloop()

