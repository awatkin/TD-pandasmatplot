import pandas as pd


# Displays the main menu and collects choice of menu item
def menu():
    flag = True

    while flag:
        print("######################Bode Parcels#########################")
        print("Welcome! Please choose an option from the list")
        print("1. Show Data for one issue")
        print("2. Under Development")

        main_menu_choice = input("Please enter the number of your choice (1-2): ")

        try:
            int(main_menu_choice)
        except Exception as e:
            print("Sorry, you did not enter a valid choice")
            print("You generated the following error: ", e)
            flag = True
        else:
            if int(main_menu_choice) < 1 or int(main_menu_choice) > 1:
                print("Sorry, you did not enter a valid choice")
                flag = True
            else:
                return int(main_menu_choice)

            # Menu item selection form user and validates it


def get_issue_choice():
    flag = True

    while flag:
        print("######################################################")
        print("Please choose an issue type from the list:")
        print("Please enter the number of the item (1-4)")
        print("1.  Delivery Issue")
        print("2.  Customer Account Issue")
        print("3.  Service Complaint")
        print("4.  Collection Issue")
        print("######################################################")

        menu_list = ["Delivery Issue", "Customer Account Issue", "Service Complaint", "Collection Issue"]

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
                item_name = menu_list[int(item_choice) - 1]
                return item_name


# imports data set and extracts data and returns data for a specific revenue stream
def get_selected_item(item):
    df1 = pd.read_csv("May25_prepdata.csv")
    df2 = df1[df1["Issue Type"] == item]

    return df2


main_menu = menu()
if main_menu == 1:

    revStream = get_issue_choice()

    extracted_data = get_selected_item(revStream)

    print("Here is the sales data for {} :".format(revStream))
    print(extracted_data)

else:
    print('This part of the program is still under development')
