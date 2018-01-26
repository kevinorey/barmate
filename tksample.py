import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):

        ## Add Liquor Button
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Add Liquor"
        self.hi_there["command"] = self.addLiquor
        self.hi_there.pack(side="top")

        ## View Liquor Button
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "View Liquor"
        self.hi_there["command"] = self.viewLiquor
        self.hi_there.pack(side="top")

        self.QUIT = tk.Button(self, text="QUIT", fg="red",
                                            command=root.destroy)
        self.QUIT.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

    def viewLiquor(self):
        print("Time to fetch liquor")

    def addLiquor(self):
        print("Time to add liquor")
        

root = tk.Tk()
app = Application(master=root)
app.mainloop()
