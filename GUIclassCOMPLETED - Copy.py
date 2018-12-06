from tkinter import *

#Create a class
class Application(Frame):
    """A GUI application."""

    def __init__(self,master):
        """Initialize the Frame"""
        Frame.__init__(self,master)
        self.grid()
        self.create_widgets()
        

    def create_widgets(self):
        """Creates 4 buttons with corressponding events"""

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
        self.button2.configure(text = "Add a Route",command = self.another_window)

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
        """Simply exits the program"""
        exit()

    def open_favorites(self):
        """Opens the favoriteroutes.txt and reads it to the shell"""
        file = open("favoriteroutes.txt","r")
        print(file.read())
        file.close

    def open_allroutes(self):
        """Opens the favoriteroutes.txt and routefile.txt files so the user can
            see all routes"""
        file = open("routefile.txt","r")
        print(file.read())
        file.close
        file = open("favoriteroutes.txt","r")
        print(file.read())
        file.close()


    def create_window(self):
        #create window
        top = Toplevel()
        top.title("Route Runner: Choose a Route")
        top.geometry("300x350")


        self.instruction = Label(top, text = "How many miles would you like to run today?")
        self.instruction.pack()

        self.mileage = Entry(top)
        self.mileage.pack()

        self.instruction1 = Label(top, text = "How long would you like to run today?")
        self.instruction1.pack()

        self.time= Entry(top)
        self.time.pack()

        self.instruction2 =Label(top, text = "What kind of Terrain would you prefer?")
        self.instruction2.pack()

        self.terrain = Entry(top)
        self.terrain.pack()

        Submitbutton = Button(top, text = "Submit",command = self.suggest)
        Submitbutton.pack()

        self.text = Text(top, width = 35, height = 5, wrap = WORD) #wrap determines how text box is wrapped
        self.text.pack()

    def suggest(self):
        how_long_mi = self.mileage.get()
        how_long_time = self.time.get()
        file = open("routefile.txt","r")
        contents = file.readlines()
        file = open("favoriteroutes.txt","r")
        fave_contents = file.readlines()

        for elements in contents:
            if how_long_mi in elements or how_long_time in elements:
                print(elements)
                self.text.insert(0.0,elements)
        for elements in fave_contents:
            if how_long_mi in elements or how_long_time in elements:
                print(elements)
                self.text.insert(0.0,elements)

    def another_window(self):
        #create window
        top = Toplevel()
        top.title("Route Runner: Choose a Route")
        top.geometry("300x350")

        self.instruction0= Label(top, text = "What is this route called?")
        self.instruction0.pack()

        self.route_name = Entry(top)
        self.route_name.pack()

        self.instruction = Label(top, text = "How many miles is the route?")
        self.instruction.pack()

        self.route_mileage = Entry(top)
        self.route_mileage.pack()

        self.instruction1 = Label(top, text = "How long does it take to run?")
        self.instruction1.pack()

        self.route_time= Entry(top)
        self.route_time.pack()

        self.instruction2 =Label(top, text = "What kind of Terrain does it have?")
        self.instruction2.pack()

        self.route_terrain = Entry(top)
        self.route_terrain.pack()

        self.instruction3 = Label(top, text = "Is this a favorite route?")
        self.instruction3.pack()

        self.route_favorite = Entry(top)
        self.route_favorite.pack()

        Submitbutton = Button(top, text = "SUBMIT",command = self.add)
        Submitbutton.pack()
        
        

    def add(self):
        routes = {}
        routes['name'] = self.route_name.get()
        routes['miles'] = self.route_mileage.get()
        routes['time'] = self.route_time.get()
        routes['terrain']=self.route_terrain.get()
        routes['favorite']=self.route_favorite.get()
        
        if routes['favorite'] == "Y":
            file = open("favoriteroutes.txt","a")
            file.write(routes['name']+" ")
            file.write(routes['miles']+" ")
            file.write(routes['time']+" ")
            file.write(routes['terrain']+" ")
            file.write("\n")

        else:

            file = open("routefile.txt","a")
            file.write(routes['name']+" ")
            file.write(routes['miles']+" ")
            file.write(routes['time']+" ")
            file.write(routes['terrain']+" ")
            file.write("\n")
        print("You made it this far.")
        

        
        

root = Tk()
root.title("Route Runner")
root.geometry("300x350")

app = Application(root)
root.mainloop()




        
