import tkinter as tk                
from tkinter import font  as tkfont
from tkinter import *
import dbutil
from liquor import Liquor
from enum import Enum

class LiquorType(Enum):
    SCOTCH = "Scotch"
    WHISKEY = "Whiskey"
    WHISKY = "Whisky"
    VODKA = "Vodka"
    GIN = "Gin"
    BOURBON = "Bourbin"
    TEQUILA = "Tequila"
        

class SampleApp(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        self.title("Welcome to BarMate")

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
    age = None
    abv = None
    liquorType = None

    def __init__(self, parent, controller):

        self.name = StringVar()
        self.brand = StringVar()
        self.age = StringVar()
        self.abv = StringVar()
        self.liquorType = StringVar()
        
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Add Liquor", font=controller.title_font)
        label.grid(row=0, column=0, pady=10)
        
        ## Liquor Name
        nameLabel = tk.Label(self, text="Name", font=controller.title_font)
        nameLabel.grid(row=2, column=0, pady=10)
        nameInput = Entry(self, textvariable=self.name, width=25)
        nameInput.grid(row=2, column=1, pady=10)

        ## Liquor brand
        brandLabel = tk.Label(self, text="Brand", font=controller.title_font)
        brandLabel.grid(row=3, column=0, pady=10)
        brandInput = Entry(self, textvariable=self.brand, width=25)
        brandInput.grid(row=3, column=1, pady=10)

        ## Liquor age
        ageLabel = tk.Label(self, text="Age", font=controller.title_font)
        ageLabel.grid(row=4, column=0, pady=10)
        ageInput = Entry(self, textvariable=self.age, width=25)
        ageInput.grid(row=4, column=1, pady=10)

        ## Liquor abv
        abvLabel = tk.Label(self, text="ABV", font=controller.title_font)
        abvLabel.grid(row=5, column=0, pady=10)
        abvInput = Entry(self, textvariable=self.abv, width=25)
        abvInput.grid(row=5, column=1, pady=10)

        ## Liquor type dropdowns
        liquorLabel = tk.Label(self, text="Type", font=controller.title_font)
        liquorLabel.grid(row=6, column=0, pady=10)

        liquorList = sorted(self.convertToList())
        self.liquorType.set(liquorList[0])
        liquorTypeMenu = OptionMenu(self, self.liquorType, *liquorList)
        liquorTypeMenu.grid(row=6, column=1, pady=10)


        ## Add to db
        addButton = tk.Button(self, text="Add", command=self.addToDB)
        addButton.grid(row=7, column=0, pady=10)
    

        button = tk.Button(self, text="Main", command=lambda: controller.show_frame("StartPage"))
        button.grid(row=8, column=0)

    def addToDB(self):
        print("Entered addTODB")
        print("Collected name = ", self.name.get())
        print("Collected brand = ", self.brand.get())
        print("Collected age = ", self.age.get())
        print("Collected abv = ", self.abv.get())
        print("Collected Liquor Type = ", self.liquorType.get())

        try:

            liquor = Liquor(self.name.get(), self.brand.get(), self.abv.get(), self.age.get(), self.liquorType.get())
            liquor.addRecordToDB()

            successLabel = tk.Label(self, text="Successfully added liquor to inventory", fg="green",font=self.controller.title_font)
            successLabel.grid(row=9, column=0, pady=10)

        except Exception as excep:
            print("Error occurred = ", excep)

            errorLabel = tk.Label(self, text="Error Occurred", fg="red",font=self.controller.title_font)
            errorLabel.grid(row=9, column=0, pady=10)
            raise Exception(excep)

    def convertToList(self):
        liquorChoices = []

        for alcoholType in LiquorType:
            liquorChoices.append(alcoholType.value)

        return liquorChoices

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
