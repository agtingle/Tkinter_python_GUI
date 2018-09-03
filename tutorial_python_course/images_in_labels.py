import Tkinter as tk
from PIL import ImageTk, Image

root = tk.Tk()
#logo = tk.PhotoImage(file='python-logo.jpg')
logo = ImageTk.PhotoImage(Image.open('python-logo.jpg')) #PIL solution

#w1 = tk.Label(root, image=logo).pack(side='right')

explanation = """At present, only GIF and PPM/PGM
formats are supported, but an interface 
exists to allow additional image file
formats to be added easily.Alternatively 
we could use python library PIL to open 
image with more format.See template in 
this script."""

#w2 = tk.Label(root, justify=tk.LEFT, padx=10, text=explanation, font=('Times New Roman', 20)).pack(side='left')

#w = tk.Label(root, justify = tk.LEFT, compound = tk.CENTER, text=explanation, font=('Times New Roman', 20), image=logo).pack(side='right')
w = tk.Label(root, justify = tk.LEFT, compound = tk.RIGHT, padx=10, text=explanation, font=('Times New Roman', 20), image=logo).pack(side='right')

root.mainloop()
