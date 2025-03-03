import pandas as pd


# Displays the main menu and collects choice of menu item
def menu():

    flag = True

    while flag:
        print("###############################################")
        print("Welcome! Please choose an option from the list")
        print("1. Show sales for a specific Revenue Stream")
        print("2. Show total sales for each revenue stream")

        main_menu_choice = input("Please enter the number of your choice (1-2): ")

        try:
            int(main_menu_choice)
        except Exception as e:
            print("Sorry, you did not enter a valid choice")
            print("You generated the following error: ", e)
            flag = True
        else:
            if int(main_menu_choice) < 1 or int(main_menu_choice) > 2:
                print("Sorry, you did not enter a valid choice")
                flag = True
            else:
                return int(main_menu_choice)    

# Menu item selection form user and validates it


def get_revstream_choice():

    flag = True

    while flag:
        print("######################################################")
        print("Please choose a revenue stream form the list:")
        print("Please enter the number of the item (1-8)")
        print("1.  Tickets")
        print("2.  Gift Shop")
        print("3.  Snack Stand")
        print("4.  Pictures")
        print("######################################################")

        menu_list = ["Tickets", "Gift Shop", "Snack Stand", "Pictures"]

        item_choice = input("Please enter the number of your choice (1-4): ")

        try:
            int(item_choice)
        except Exception as e:
            print("Sorry, you did not enter a valid choice")
            print("The following error was generated: ", e)
            flag = True
        else:
            if int(item_choice) < 1 or int(item_choice) > 4:
                print("Sorry, you did not enter a valid choice")
                flag = True
            else:
                item_name = menu_list[int(item_choice)-1]
                return item_name


# imports data set and extracts data and returns data for a specific revenue stream
def get_selected_item(item):
  
    df1 = pd.read_csv("Task4_tester.csv") 
    df2 = df1[['Day', 'Time', item]]

    return df2

     
main_menu = menu()
if main_menu == 1:

    revStream = get_revstream_choice()
 
    extracted_data = get_selected_item(revStream)

    print("Here is the sales data for {} :".format(revStream))
    print(extracted_data)

else:
    print('This part of the program is still under development')
