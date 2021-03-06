import Tkinter as tk
import random

window = tk.Tk()
window.title('Greetings ______')
window.geometry('400x400')

# Functions
def phrase_generator():
    phrases = ['Hello ', 'What\'s up ', 'Farewell ', 'Hi ']
    name = str(entry1.get())
    return phrases[random.randint(0, 4)] + name

def phrase_display():
    greeting = phrase_generator()

    # This creates the text field
    greeting_display = tk.Text(master=window, height=10, width=30)
    greeting_display.grid(column=0, row=3)

    greeting_display.insert(tk.END, greeting)


# Labels
label1 = tk.Label(text='Welcome to my app!')
label1.grid(column=0, row=0)

label2 = tk.Label(text='What is your name?')
label2.grid(column=0, row=1)

# Entry fields
entry1 = tk.Entry()
entry1.grid(column=1, row=1)

# Button
button1 = tk.Button(text='CLICK ME!', command=phrase_display)
button1.grid(column=0, row=2)


window.mainloop()
