from tkinter import Tk, StringVar, Spinbox

class EntryWidgets: 

    def __init__(self, master):

        self.master = master
        master.title("Entering single-line text with the Entry Widget")

        self.month = StringVar()
        self.combobox = Combobox(master, textvariable= self.month)
        self.combobox.pack()
        
        


      

root = Tk()
my_gui = EntryWidgets(root)
root.mainloop()