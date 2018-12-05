# GUIPrototypeI
Unfinished GUI w/ View all Routes, Favorites, and Quit Functionality
README
Karena Garcia and Naomi Cebula

RouteRunner Application
----
This project aims to aid cross-country runners (or casual runners who want a helpful tool) in the process of choosing a route. The program runs in an easy-to-understand format with simple, intuitive user interaction. 

RouteRunner allows users to input new routes into a file listing all routes (adding details such as terrain, time, distance, whether or not it is a favorite route, and the name of the route.

Another feature of the application is choosing a route. The program allows users to input features of their desired run, such as desired distance, time spent running, and ideal terrain, and the program prints out a route matching those features from the file containing the list of routes. 

RouteRunner also allows the user to print out the total contents of the list containing all routes, essentially printing all routes to the screen. It also allows the user to selectively print only routes sorted into Favorite Routes in their own list using the Favorites button. 

RouteRunner also has a Quit button to quit the program.
----
To run the program, currently the program runs in two parts. To run the section with the Graphics interface and some functionality, run GUIclass.py . This opens the main window with the buttons Choose Route, Add Route, View Routes, Favorites, and Quit. Quit, View Routes, and Favorites currently work, while Add Route and Choose Route are still under construction. To run the program with full functionality, run PrototypeII.py and when prompted for input, follow the written instructions.
----
GUItextEntry.py, GUIclass.py and PrototypeII.py need to be downloaded for RouteRunner to work. Also be sure that routefile.txt and favoriteroutes.txt are downloaded into the same folder; the program stores key data in these text files.

TKinter is already built into Python, so that module does not need outside downloading.
----
KNOWN BUGS:
1. in PrototypeII, when the user is inputting the values for length of route and time of run, the user has to manually type out, for example, "six miles" as opposed to 6 or 6 miles, otherwise the program can potentially get confused if there is a 6 in the "time of route" value.
2. We are still having trouble getting the Choose Route and Add Route buttons in GUIClass to function.
