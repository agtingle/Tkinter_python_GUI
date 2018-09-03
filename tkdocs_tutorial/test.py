from Tkinter import *
import ttk

root = Tk()
root.title('test GUI')
root.geometry('300x300')

#measureSystem = StringVar()

#check = ttk.Checkbutton(root, text='Use Metric', command=metricChanged, variable=mesureSystem, onvalue='metric', offvalue='imperical')
#check.grid()

phone = StringVar()
home = ttk.Radiobutton(root, text='Home', variable=phone, value='home').grid()
office = ttk.Radiobutton(root, text='Office', variable=phone, value='office').grid()
cell = ttk.Radiobutton(root, text='Mobile', variable=phone, value='cell').grid()



phone_entry = ttk.Entry(root, width=7, textvariable=phone)
phone_entry.grid()

root.mainloop()
