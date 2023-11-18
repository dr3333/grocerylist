import csv
import re
import sys
from art import tprint
from clses import Item, List
from tabulate import tabulate
from helper import home_help_cmds, cur_help_cmds, print_border_help, print_border_1, print_space

#Save file name
save_file_name = "gl_save"


def main():
    load_list_f()
    tprint("GROCERY     LIST.")
    home_input()


################### HOME ############################
def home_input():#Home USER INPUT menu
    print("type /help for more info")
    while True:
        user_input = input("Input: ")
        if user_input == "/help":#Help commands
            home_cmds()

        if user_input == "/newlist":#Create New file
            new_list()

        if user_input == "/showlists":#show all available lists
            show_list_table()

        if user_input == "/open":#open list
            show_list_table()
            open_list()

        if user_input in ["/rmitem", "/additem", "/deleteitem" ,"/showitems", "/currentlist"]:#prompt use to open a list first
            print("Open a List first")

        if user_input == "/deletelist": #Delete a list
            show_list_table()
            while True:
                lname = input("Input list to delete: ")
                if lname == "/back":
                    break
                if List.get_list(lname):
                    del_list(lname)
                    break

        if user_input == "/exit": #Exit program
            exit_program()


def home_cmds(): #LIST of COMMANDS for HOME
    print(print_border_help)
    for hc in home_help_cmds:
        print(hc)
    print(print_border_1)


def del_list(lname):#Delete List
    while True:
        confirm_input = input(f"Are you sure you want to delete List '{lname}'? 'yes' or 'no' or y or n: ")

        if re.match(r'^(y|yes)$', confirm_input, re.IGNORECASE):
            List.delete_list(lname)
            print(f"List '{lname}' has been deleted.")
            save_list_f()
            return
        elif re.match(r'^(n|no)$', confirm_input, re.IGNORECASE):
            return
        else:
            print("Invalid Input. Please enter 'yes' or 'no' or 'y' or 'n'")


def show_list_table():#Print list of lists
    ll = List.get_all_lnames()
    print(tabulate(ll, headers = "keys", tablefmt="grid"))


def new_list(): #CREATE NEW LIST
    while True:
        u_input = input(f"List Name: ")
        if u_input == "/back":
            return

        if re.match(r"^(?!/).*$", u_input):
            if List.get_list(u_input):
                print("List already exist")
            elif not List.get_list(u_input):
                List(u_input)
                print(f"New List {u_input} created")
                cur_list_input(f"{u_input}")
                break
        else:
            print("List name cannot start with '/'.")


def open_list(): #OPEN LIST
    while True:
        u_input = input(f"List Name: ")
        if u_input == "/back":
            return
        if not List.get_list(u_input):
            print(f"List: {u_input} does not exist")
        elif List.get_list(u_input):
            break
    cur_list_input(u_input)


################### CURRENT LIST ############################
def cur_list_input(lname):#CURRENT LIST PAGE
    list_name_header(lname)
    print("type /help for more info")
    while True:
        u_input = input(f"||{lname}|| Input: ")
        if u_input == "/back":#back to home
            break

        if u_input == "/additem":#add item to list or amount to an item in list
            cur_add_item(lname)
            save_list_f()

        if u_input == "/rmitem":#remove a certain amount of an item from list
            cur_rm_item(lname)
            save_list_f()

        if u_input == "/deleteitem":#delete an item from current list
            del_item(lname)
            save_list_f()

        if u_input == "/showitems":#show items in a table
            show_item_table(lname)

        if u_input == "/showlists":
            show_list_table()

        if u_input == "/deletelist":#Delete current list
            del_list(lname)
            save_list_f()
            break

        if u_input == "/newlist":#Create New file
            new_list()

        if u_input == "/open":#open list
            show_list_table()
            open_list()
            break

        if u_input == "/currentlist":#Show current list
            list_name_header(lname)

        if u_input == "/help":#show the list of commands for current list
            cur_cmds()

        if u_input == "/exit": #Exit program
            exit_program()
    return


def cur_cmds():#Help commands for current list
    print(print_border_help)
    for hc in cur_help_cmds:
        print(hc)
    print(print_border_1)


def show_item_table(lname):#Show item table or list
    ls = List(lname)
    itms = ls.return_bucket()
    print(tabulate(itms, headers = "keys", tablefmt="grid"))


def cur_add_item(lname): #Current list add item
    ls = List(lname)
    while True:
        show_item_table(lname)
        while True:
            name = input(f"||{lname}||ADD|| Item Name: ")
            if name == "/back":
                return
            if re.match(r"^(?!/).*$", name):
                break
            else:
                print("Item can not start with '/'")

        while True:
            try:
                amt = input(f"||{lname}||ADD|| {name} Amount: ")
                if amt == "/back":
                    return
                amt = int(amt)
                if isinstance(amt, int):
                    itm = Item(name, amt)
                    ls.add_item(itm)
                    print(f"Item: {name} Amount: {amt} was added to {lname}")
                    break
            except ValueError:
                print("Amount must be a non fraction number")


def cur_rm_item(lname):#Current list remove item
    ls = List(lname)
    while True:
        show_item_table(lname)
        while True:
            name = input(f"||{lname}||Remove|| Item Name: ")
            if name == "/back":
                return
            if re.match(r"^(?!/).*$", name): #check if name starts with /
                if name == ls.check_bucket(name):
                    break
            else:
                print("Item can not start with '/'")

        while True:
            try:
                amt = input(f"||{lname}||Remove|| {name} Amount: ")
                if amt == "/back":
                    return
                amt = int(amt)
                if isinstance(amt, int):
                    itm = Item(name, amt)
                    ls.remove_item_amt(itm)
                    print(f"Item: {name} Amount: {amt} was removed from {lname}")
                    break
            except ValueError:
                print("Amount must be a non fraction number")


def del_item(lname):#Delete item from list
    show_item_table(lname)
    while True:
        itm_name = input(f"||{lname}||Del|| Item Name: ")
        if itm_name == "/back":
            return
        ls = List(lname)
        if itm_name == ls.check_bucket(itm_name):
            while True:
                confirm_input = input(f"Are you sure you want to delete List '{itm_name}'? 'yes' or 'no' (y/n): ")

                if re.match(r'^(y|yes)$', confirm_input, re.IGNORECASE):
                    ls.delete_item(itm_name)
                    print(f"Item '{itm_name}' has been deleted.")
                    return
                elif re.match(r'^(n|no)$', confirm_input, re.IGNORECASE):
                    return
                else:
                    print("Invalid Input. Please enter 'yes' or 'no' or 'y' or 'n'")


################### SAVE AND LOAD ############################
def load_list_f():#LOAD LIST
    try:
        fname = f"{save_file_name}.csv"
        with open(fname, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                r = Item(row["name"], row["amount"])
                l = List(row["lname"])
                l.add_item(r)
    except FileNotFoundError:
        save_list_f()


def save_list_f(): #save to file
    try:
        fname = f"{save_file_name}.csv"
        with open(fname, "w") as file:
            writer = csv.DictWriter(file, fieldnames=["lname", "name", "amount"])
            writer.writeheader()
            d_data = []
            d_data = List.get_csv_data()
            for itm in d_data:
                writer.writerow(itm)
    except Exception as e:
        print(f"Error saving data to CSV file: {e}")
    return


################### Utility ############################
def list_name_header(lname):
    print(print_border_1)
    print(f"{print_space}List: {lname}")
    print(print_border_1)


def exit_program():
    print("Saving File")
    save_list_f()
    sys.exit("Exiting. Good bye.")


if __name__ == "__main__":
    main()
