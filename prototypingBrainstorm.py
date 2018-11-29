option = input("What would you like to do? (CHOOSE, ADD, FAVORITES, VIEW, QUIT: ").upper()
route_list = []
routes = {}

while option != "QUIT":

    if option == "ADD":
        routes['name'] = input("Name: ")
        routes['miles'] = input("Length in Mileage: ")
        routes['time'] = input("Time in Minutes: ")
        routes['terrain']=input("Terrain (Grass, Gravel, Asphalt, Pavement): ")
        routes['favorite']=input("Is this a Favorite Route?(Y/N): ").upper()

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


    elif option == "VIEW":
        file = open("routefile.txt","r")
        print(file.read())
        file.close
        file = open("favorite.txt","r")
        print(file.read())
        file.close()

    elif option == "FAVORITES":
        file = open("favoriteroutes.txt","r")
        print(file.read())

    else: #instead of writing just 6 put six miles...when adding it to 6 miles  
        mileage = input("How far would you like to run today in miles?: ")
        time = input("How long would you like to run in minutes?: ")
        file = open("routefile.txt","r")
        contents = file.readlines()
        file = open("favoriteroutes.txt","r")
        fave_contents = file.readlines()
        for elements in contents:
            if mileage in elements or time in elements:
                print(elements)
        for elements in fave_contents or time in elements:
            if mileage in elements:
                print(elements)
        
        
    option = input("What would you like to do? (CHOOSE, ADD, REMOVE, FAVORITES, VIEW, QUIT: ").upper()
    
    #References: YouTube playlist assignment and lab inspired the design and logic
    
    
    
    
