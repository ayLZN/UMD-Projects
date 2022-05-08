# INST_326_Project

Libraries to import
-----------
pip install tkinter 

pip install json

pip install requests

pip install random

pip install tkcalendar

Quick Start 
-----------
Please add the api key on Line 8 in get_address.py !

When entering in an address please use this setup : 101 Halpine Road Rockville MD 
Please capitalize first letter in every word. Two state letter abbreviation should be Capitalized.

Enter category for  "type of place"  can be hardware,eletronics, restaurants, groceries and so on.
Enter category for "item type" can be word related to "type of place".

For example, If you were to put hardware for type of place, you can enter Drywall, hammer, wood, chainsaw, or lightbulbs.


Script requires api which is a global variable. 

Unit Tests
-----------
If a user enters an invalid address, “place” or “item” - code will prompt invalid entry.

Invalid entry. Please enter a proper address with this format:101 Halpine Road Rockville MD For place and item: enter one word (restaurant , hardware etc) for item enter: japanese,american, indian, etc for restaurant. hammer, drywall, plumbing, etc for hardware.


Documentation
-----------
One to four sentences explaining what your project is and what it does.
Our project is a program which emulates a delivery application. A user will be able to select an item for delivery and get said item delivered to them. This is done by our application asking a user to enter various data (addresses, contact info, etc) and then, by utilizing our algorithms and functions, our app will create a dynamic receipt with relevant information (such as time for delivery and price).

An explanation on how to run the program from the command line.

python3 gui.py

Documentation on how to use the program / how to interpret the output of the program.
Our program was made with the intention of being easy to use. In order to use our delivery app, our program simply requires a user to enter the relevant information into the shown entry box. 
Drop off location  - 					Enter text
Enter place category - 					Enter text
Enter item type - 					Enter text
Full name | email | phone | date to make delivery - 	Enter text
4a.  Date to make delivery - 					Select from calendar tool
Enter store to get item(s) from - 				Select from drop down menu

Once all of the user entry is complete, a receipt will be shown with very easily interpretable results. Each information item on the receipt will be displayed as . . . Variable name: user entry
An annotated bibliography of all sources you used to develop the program and how you used them.


Annotated Bibliography
-----------

“Google APIs Explorer.” Google.com, 2019, developers.google.com/apis-explorer/. Accessed 3 Feb. 2019.


This website provides various insights into Google Geocode, Place, and Direction API’s. We utilized these various application programming interfaces so that we would be able to provide real-life utility in our code from travel time to store locations in a user’s proximity. This was extremely useful and necessary for our program.


TKinter.com – Learn to Build GUI Apps WIth Tkinter and Python! tkinter. com

This website provides various insights into the Tkinter library within python. We utilized this website in order to better educate ourselves with regards to the versatility and implementation factors which Tkinter has to offer. The usage of the information obtained from this site is most prominent in our GUI. Though very useful and informative, minor additional resources were required for further Tkinter usage within our program.




