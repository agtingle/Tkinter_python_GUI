## Q&A while using Python GUI library Tkinter

* Q: Why couldn't I import python library tkinter even if it is well installed?

  A: This might be a capital problem:

```python
try:
    import Tkinter as tk #this is for python2
except:
    import tkinter as tk #this is for python3
```

        If this doesn't work, try reinstalling tkinter.

* Q: Why couldn't tkinter recognize a png or jpg format image?

  A: Unfortunately It is... At present only GIF and PPM/PGM formats are supported,however you could make it as follows(There are some alternative choices,not only this one):

  ```python
  import Tkinter as tk
  from PIL import ImageTk, Image
  root = tk.Tk()
  logo = ImageTk.PhotoImage(Image.open('python-logo.jpg'))
  label1 = tk.Label(root, image=logo)
  root.mainloop()
  ```
