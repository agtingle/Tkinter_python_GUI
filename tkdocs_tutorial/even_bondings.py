from Tkinter import *
import ttk

root = Tk()
root.title('Event Binding test')
root.geometry('400x400')
tmp = ttk.Label(root, text='Starting...', font=('Times New Roman', 25))

tmp.grid(column=1, row=1)

tmp.bind('<Enter>', lambda e: tmp.configure(text='Move mouse inside'))
tmp.bind('<Leave>', lambda e: tmp.configure(text='Move mouse outside'))
tmp.bind('<1>', lambda e: tmp.configure(text='Click left mouse button'))
tmp.bind('<Double-1>', lambda e: tmp.configure(text='Doulble clicked'))
tmp.bind('<B3-Motion>', lambda e: tmp.configure(text='right button drag to %d,$d' % (e.x, e.y)))

root.mainloop()
