
from tkinter import Button, PhotoImage, Tk
from tkinter.constants import RIGHT

class ButtonLabel: 

    def __init__(self, master):

        self.master = master
        master.title("Capturing input with Buttons")

        # Create a button with the class Button
        self.button = Button(master, text='Click Me ', font= ('Arial', 16 , 'bold'))
        self.button.pack()
        # assing a function with 'command' parameter
        self.button.config(command=self.callback)
        # Simulate a button click
        self.button.invoke()
        # Disable button
        self.button.config(state='disable')
        # Back to normal button
        self.button.config(state='normal')


        # Assing image path
        self.logo = PhotoImage(file= "C:\\Users\\marce\\Google Drive\\PROGRAMMING\\CURSOS\\LINKEDIN LEARNING\\Become a Python Developer\\Python GUI Development with Tkinter\\python-dev-gui-tkinter\\images\\python.gif")
        # Resize logo
        self.small_logo = self.logo.subsample(30,30)
        # put logo inside the button, on the right side
        self.button.config(image=self.small_logo, compound= RIGHT)
        
    def callback(self):
        print('Clicked')
        

root = Tk()
my_gui = ButtonLabel(root)
root.mainloop()