#Import tkinter which is built-in Python
#No need to download any external file/module
from tkinter import *

#Class is created for the main frame.
class Application(Frame):
    """A GUI appllication."""

    def __init__(self,master):
        """Initialize the Frame"""
        Frame.__init__(self,master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """Creates a home menu where the user has a choice of buttons and corressponding events"""

        #Create instruction labels for the entry box
        self.instruction = Label(self,text = "How many miles would you like to run today? (Ex: 6 miles)")
        self.instruction1 = Label(self, text = "How many minutes would you like to run today? (Ex: 50 minutes)")

        #Put those instruction in a specific spot on the grid
        self.instruction.grid(row=0,column=0, columnspan = 2, sticky = W) # W=west (rightside)
        self.instruction1.grid(row = 2, column = 0, columnspan = 2, sticky = W)

        #Create a text entry box
        self.mileage = Entry(self)

        #Put that entry box in a certain position
        self.mileage.grid(row = 1, column = 1, sticky = W)

        #Create a text entry box
        self.time = Entry(self)

        #Put it on the grid
        self.time.grid(row = 3, column = 1, sticky = W)

        #Create a submit button and put it on the grid
        self.submit_button = Button(self, text = "Submit", command = self.suggest)
        self.submit_button.grid(row = 5, column = 1, sticky = W)

        #Put a text box of a certain width and height that wraps around the words printed to it.
        self.text = Text(self, width = 35, height = 5, wrap = WORD) #wrap determines how text box is wrapped
        self.text.grid(row = 6, column = 0, columnspan = 2, sticky = W)

    def suggest(self):
        """This gets the entry from create_widgets and uses it to suggest a route from the files
            as it checks the files for the text entered."""

        #These variables get the text entered in create_widgets
        how_long_mi = self.mileage.get()
        how_long_time = self.time.get()
        file = open("routefile.txt","r")
        contents = file.readlines()
        file = open("favoriteroutes.txt","r")
        fave_contents = file.readlines()

        #Check the contents list for the mileage of time the user wants to run, and if it's in the list, suggest that route.
        for elements in contents:
            if how_long_mi in elements or how_long_time in elements:
                print(elements)

        self.text.insert(0.0,elements)

root = Tk()
root.title("Route Runner")
root.geometry("600x400")

app = Application(root)
root.mainloop()
