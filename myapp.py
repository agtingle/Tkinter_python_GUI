try:
    import Tkinter as tk #for python2
except:
    import tkinter as tk #for python3

window = tk.Tk()
# Adds a title to the window
window.title('My APP!')

# Sizes the window when first appears, measured in pixels
window.geometry('400x350')

# Labels
prompt =tk.Label(text = 'Hello world.\n Welcome to my app!', font=('Times New Roman', 20))
prompt.grid()

# Entry fields
entry_field1 = tk.Entry()
entry_field1.grid()

# Buttons
button1 = tk.Button(text='Click me!', bg='red')
button1.grid()

# Text fileds
text_field = tk.Text(master=window, height=10, width=30)
text_field.grid()

window.mainloop() #put the configuration between .Tk() and .mainloop() otherwise it would work
