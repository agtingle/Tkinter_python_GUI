from Tkinter import *
import tkFileDialog, ttk

root = Tk()
#printmsg=StringVar()
root.filename = tkFileDialog.askopenfilename(initialdir = '/', title = 'Select file', filetypes = (('jpeg files', '*,jpg'),('all files', '*.*')))

filenamelist = []
filenamelist.append(root.filename.split('/')[-1])
print filenamelist[0]
#printmsg.set("The chosen file names %s" % root.filename)
#sentlbl = ttk.Label(root, textvariable=printmsg, anchor='center')

