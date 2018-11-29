from tkinter import *

class Application(Frame):
    """A GUI appllication."""

    def __init__(self,master):
        """Initialize the Frame"""
        Frame.__init__(self,master)
        self.grid()
        self.create_widgets()
        

    def create_widgets(self):
        """Create 4 buttons"""

        #label 1
        self.label = Label(self, text = "Welcome to Route Runner!")
        self.label.grid()

        #label 2
        self.label2 = Label(self, text = "What would you like to do?")
        self.label2.grid()
        
        #button 1
        self.button1 = Button(self,text = "Choose a Route",command=self.create_window)
        self.button1.grid()

        #button 2
        self.button2 = Button(self)
        self.button2.grid()
        self.button2.configure(text = "Add a Route")

        #button 3
        self.button3 = Button(self)
        self.button3.grid()
        self.button3.configure(text = "View all Routes", command = self.open_allroutes)

        #button 4
        self.button4 = Button(self)
        self.button4.grid()
        self.button4.configure(text = "Favorites",command=self.open_favorites)
        

        #button 5
        self.button5 = Button(self)
        self.button5.grid()
        self.button5.configure(text = "Quit",command= self.client_exit)

    def client_exit(self):
        exit()

    def open_favorites(self):
        file = open("favoriteroutes.txt","r")
        print(file.read())
        file.close

    def open_allroutes(self):
        file = open("routefile.txt","r")
        print(file.read())
        file.close
        file = open("favoriteroutes.txt","r")
        print(file.read())
        file.close()

    def create_window(self):
        
        #create window
        root = Tk()
        root.title("Route Runner: Choose a Route")
        root.geometry("300x350")
        

        #entry box1
        mileage_entry = Entry()
        mileage_entry.grid()

        app = Frame(root)
        app.grid()
        root.mainloop()

        
        

root = Tk()
root.title("Route Runner")
root.geometry("300x350")

app = Application(root)
root.mainloop()

#References: https://www.youtube.com/watch?v=HVQeV7xe310
#investary tkinter YouTube Tutorials 34-38


        
