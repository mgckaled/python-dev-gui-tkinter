from tkinter import Checkbutton, Radiobutton, StringVar, Tk

class CheckRaddioButtons: 

    def __init__(self, master):

        self.master = master
        master.title("Presenting choices with check buttons and radio buttons")

        # Create a checkbutton and show in window
        self.checkbutton = Checkbutton(master, text='SPAN? ', font= ('Arial', 12 , 'bold'))
        self.checkbutton.pack()

        self.spam = StringVar()
        self.spam.set('SPAM!')
        self.spam.get()

        self.checkbutton.config(text= "Span", variable=self.spam, onvalue="Span Please", offvalue= "Boo Span")
        print(self.spam.get())
        print(self.spam.get())


        self.breakfast = StringVar()
        self.radiobutton = Radiobutton(root, text= "SPAM", variable=self.breakfast)
        self.radiobutton.pack()

        self.rbeggs = Radiobutton(root, text= "Eggs", variable=self.breakfast, value= 'Eggs')
        self.rbeggs.pack()

        self.rbsausage = Radiobutton(root, text= "Sausage", variable=self.breakfast, value= 'Sausage')
        self.rbsausage.pack()

        self.rbspan = Radiobutton(root, text= "SPAM", variable=self.breakfast, value= 'SPAM')
        self.rbspan.pack()

        self.breakfast.get()
        self.checkbutton.config(variable=self.breakfast)


        

root = Tk()
my_gui = CheckRaddioButtons(root)
root.mainloop()