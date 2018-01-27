import tkinter as tk                
from tkinter import font  as tkfont
from tkinter import *


class SampleApp(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, ViewLiquor, AddLiquor):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is the start page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="View Liquor",
                            command=lambda: controller.show_frame("ViewLiquor"))
        button2 = tk.Button(self, text="Add Liquor",
                            command=lambda: controller.show_frame("AddLiquor"))
        button1.pack()
        button2.pack()


class ViewLiquor(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="View Available Liquor", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Main",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


class AddLiquor(tk.Frame):

    name = None
    brand = None

    def __init__(self, parent, controller):

        self.name = StringVar()
        self.brand = StringVar()
        
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Add Liquor", font=controller.title_font)
        label.grid(row=0, column=0, pady=10)
        
        ## Liquor Name and Input
        nameLabel = tk.Label(self, text="Name", font=controller.title_font)
        nameLabel.grid(row=2, column=0, pady=10)
        nameInput = Entry(self, textvariable=self.name, width=25)
        nameInput.grid(row=2, column=1)

        ## Liquor brand and Input
        brandLabel = tk.Label(self, text="Brand", font=controller.title_font)
        brandLabel.grid(row=3, column=0, pady=10)
        brandInput = Entry(self, textvariable=self.brand, width=25)
        brandInput.grid(row=3, column=1)
        

        addButton = tk.Button(self, text="Add", command=self.addToDB)
        addButton.grid(row=4, column=0, pady=10)
    

        button = tk.Button(self, text="Main", command=lambda: controller.show_frame("StartPage"))
        button.grid(row=5, column=0)

    def addToDB(self):
        print("Entered addTODB")
        print("Collected name = ", self.name.get())
        print("Collected brand = ", self.brand.get())



if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
