# **Grocery List**
#### Video Demo: https://youtu.be/cTbzfjoCB1k
#### Description: A command-line grocery list mangement system
#### Files
##### project.py: This is where the main code is located
##### helper.py: This is where variables that help main.py function properly
##### clses.py: This contains the class Item and class List
##### gl_save.py: This is where the list data are stored
#### Commands
##### /help
###### This command will output a list of commands. When ran in the Home page it will output all the commands that can be ran in the Home page. When ran in the current list page it will show all the commands that can be ran in the current list page.
##### /newlist
###### This command creates a new list. It can be used in the home page and the current list page.
##### /open
###### This command shows you a table of all the lists you have and opens list. Once an existing list has been inputted, it will take you to the current list page of that list. It can be used in the home page and the current list page.
##### /showlists
###### This command shows a table of all the lists you have.
##### /additem
###### This command adds an item and amount to the current opened list. It will keep prompting user for the name of the item and an amount until the you run /back. This command can only be ran in the current list page, else it will prompt you to open a list first.
##### /rmitem
###### This command removes an amount from an item in the current opened list. It will keep prompting user for the name of the item and an amount until the you run /back. If you remove more than the list contain it will automatically delete the item. This command can only be ran in the current list page, else it will prompt you to open a list first.
##### /deleteitem
###### This command deletes an item from the current list opened. This command can only be ran in the current list page, else it will prompt you to open a list first.
##### /showitems
###### This command shows a table of all the items in the list with their amounts. This command can only be ran in the current list page, else it will prompt you to open a list first.
##### /currentlist
###### This command shows the current list that is opened. This command can only be ran in the current list page, else it will prompt you to open a list first.
##### /deletelist
###### This command deletes a list. If you run it in the home page it will show you the list of lists. If you run it in the current list page it will delete the current list.
##### /exit
###### This command exits saves the the lists and item to the save file and exits the program. It can be ran from both the current page and the home page.
#####
##### Modules
###### art
###### csv
###### re
###### sys
###### tabulate
