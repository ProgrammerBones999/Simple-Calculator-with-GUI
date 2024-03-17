mport tkinter as tk

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

# create the application
calculator = App()

#
# here are method calls to the window manager class
#
myapp.master.title("Calculator")
myapp.master.maxsize(1080, 720)

# start the program
calculatpr.mainloop()
