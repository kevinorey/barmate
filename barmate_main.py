import tkinter as tk
import liquor

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):

        #Create view liquor button
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "View"
        self.hi_there["command"] = self.viewLiquor
        self.hi_there.pack(side="top")

        #Create add liquor button
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Add"
        self.hi_there["command"] = self.addLiquor
        self.hi_there.pack(side="top")

        self.QUIT = tk.Button(self, text="Quit", fg="red",
                                            command=root.destroy)
        self.QUIT.pack(side="bottom")

    def viewLiquor(self):
        print("Entered View Liquor")

    def addLiquor(self):
        print("Entered Add Liquor")


root = tk.Tk()
app = Application(master=root)
app.mainloop()
