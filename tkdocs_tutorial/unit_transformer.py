from Tkinter import *
import ttk

def calculate(*args):
    try:
        value = float(hartree.get())
        electronvolt.set(27.211 * value)
    except ValueError:
        pass
    
root = Tk()
root.title("Hartree to Electronvolt")

#Frame
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

#Tkinter only allows you to attach to an instance of the "StringVar" class
hartree = StringVar()
electronvolt = StringVar()

#Entry_field
hartree_entry = ttk.Entry(mainframe, width=7, textvariable=hartree)
hartree_entry.grid(column=2, row=1, sticky=(W, E))

#Label and Button
ttk.Label(mainframe, textvariable=electronvolt).grid(column=2, row=2, sticky=(W, E)) #'textvariable=electronvolt' :show text which is a variable called 'electronvolt'
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="Hartree").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="eV").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

hartree_entry.focus()
root.bind('<Return>', calculate)

root.mainloop()
