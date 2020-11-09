from tkinter import Tk, Label
from tkinter.constants import CENTER

class DislpayLabel: 

    def __init__(self, master):
        self.master = master
        master.title("Displaying text and images with Labels")

        self.label = Label(master, text="Hello Tkinter")
        self.label.pack()

        self.label.config(text="I just have changed the text. This is an amazing OOP program")
        # Wrap the text, passing number of pixels
        self.label.config(wraplength=150)
        # Justify text
        self.label.config(justify=CENTER)
        # Setup colors
        self.label.config(foreground='blue', background='yellow')
        # Setup font -> passing a set of elements
        self.label.config(font= ('Courier', 18, 'bold'))
        

root = Tk()
my_gui = DislpayLabel(root)
root.mainloop()