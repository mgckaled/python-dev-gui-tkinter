from tkinter import Entry, Tk
from tkinter.constants import END

class EntryWidgets: 

    def __init__(self, master):

        self.master = master
        master.title("Entering single-line text with the Entry Widget")

        # Entry Class
        self.entry = Entry(master, width=40, )
        self.entry.pack()
        # Insert a pre-defined text
        self.entry.insert(0, 'Example')
        # Delete 1 character
        self.entry.delete(0, 1)
        # Delete the entire text 
        self.entry.delete(0, END)
        
        # place a specified content
        self.entry.insert(0, 'Enter your password')
        self.entry.config(show= '*')
        # show the real content
        print(self.entry.get())

        # Disabe entry 
        self.entry.config(state= 'disable')
        # Enable entry
        self.entry.config(state='normal')

      

root = Tk()
my_gui = EntryWidgets(root)
root.mainloop()