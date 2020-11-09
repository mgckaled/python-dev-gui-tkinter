
# ttk is a module from tkinter package
from tkinter import *
from tkinter import ttk

# *************************************
# Tk() - Constroctor method
# Will create a top level window 
# *************************************
root = Tk()


button = ttk.Button(root, text="Click me!")
# pack() method will display button on window
button.pack()
# Change the text button
button.config(text="Push Me")

print(button.config())
print("")
print(str(button))
print(str(root))

ttk.Label(root, text="Hello Tkinter").pack()

root.mainloop()
