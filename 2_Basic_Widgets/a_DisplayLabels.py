from tkinter import PhotoImage, Tk, Label
from tkinter.constants import CENTER

class DislpayLabel: 

    def __init__(self, master):

        self.master = master
        master.title("Displaying text and images with Labels")

        # *******************
        # TEXT
        # *******************
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
        
        # *******************
        # IMAGE
        # *******************

        # Assign image path
        self.logo = PhotoImage(file= "C:\\Users\\marce\\Google Drive\\PROGRAMMING\\CURSOS\\LINKEDIN LEARNING\\Become a Python Developer\\Python GUI Development with Tkinter\\python-dev-gui-tkinter\\images\\python.gif")
        #Resize logo
        self.small_logo = self.logo.subsample(5,5)
        # Put logo in label
        self.label.config(image = self.small_logo)
        self.label.config(compound='left')

        
root = Tk()
my_gui = DislpayLabel(root)
root.mainloop()