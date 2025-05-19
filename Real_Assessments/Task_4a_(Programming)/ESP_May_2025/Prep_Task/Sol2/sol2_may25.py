import pandas as pd
import matplotlib.pyplot as plt  # Added This import to allow use of graphing


# This is the solution to Task 1 AND Task 2
# The tasks are:
# Task 1 - The total number of each issue type and the average rating for that problem
# Task 2 - The Number of Parcels effected for each Issue Type
# All changes have comments on / around them to show them

# Displays the main menu and collects choice of menu item
def menu():
    flag = True

    while flag:
        print("######################Bode Parcels#########################")
        print("Welcome! Please choose an option from the list")
        print("1. Show Data for one issue")
        print("2. Issue Numbers and rating (TASK 1)")  # updated this line to accomodate task 1 option
        print("3. No, Of Parcels for each issue (TASK 2)")  # added a new entry for task 2 selection

        main_menu_choice = input("Please enter the number of your choice (1-3): ")  # updated this line to accomodate further than option 2

        try:
            int(main_menu_choice)
        except Exception as e:
            print("Sorry, you did not enter a valid choice")
            print("You generated the following error: ", e)
            flag = True
        else:
            if int(main_menu_choice) < 1 or int(main_menu_choice) > 3:  # further updated this to allow higher than 2
                print("Sorry, you did not enter a valid choice")
                flag = True
            else:
                return int(main_menu_choice)

            # Menu item selection form user and validates it


def parcels_effected():  # new subroutine to solve task 2
    df = pd.read_csv("May25_prepdata.csv")  # read in a fresh clean dataframe
    effected = df[["Issue Type", "No Of Parcels"]]  # reduces down the df to just needed columns
    effected = effected.groupby(["Issue Type"])["No Of Parcels"].sum()  # this groups by issue type and totals the number of parcels
    print("The Number parcels for each issue Type is: ")
    print(effected)  # this outputs the count of each parcel count type

    effected.plot.bar()  # sends the data set to the matplot lib grapher
    plt.title("Total Parcels per Issue")  # sets the title
    plt.show()  # shows the plot

def issue_rating_counter():  # added a new subroutine to solve the task 1 problem
    df = pd.read_csv("May25_prepdata.csv")  # read in a fresh clean dataframe
    issue_counts = df[["Issue Type"]].value_counts()  # This reduces the dataframe to just the Issue type column then counts each issue type
    print("The Number of each issue Type is: ")
    print(issue_counts)   # this outputs the count of each issue type
    rating_count = df[["Issue Type", "Rating"]]  # This reduces the df to just the 2 cols needed
    rating_count = rating_count.groupby("Issue Type")  # Then groups the data  by issue type
    rating_count = rating_count["Rating"].mean() # then applies an average to the rating for each issue type.
    print("The average Rating of each issue Type is: ")
    print(rating_count)  # outputs the results.

    # Graphing the data out.
    issue_counts.plot.bar()  # sends the data set to the matplot lib grapher
    plt.title("Total Issue Numbers")  # sets the title
    plt.show()  # shows the plot

    rating_count.plot.bar()  # sends the data to the matplot lib grapher
    plt.title("Rating of Issue Types")  # sets the title
    plt.show()   # shows the data,

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

elif main_menu == 2:  # added a new selection statement for task 1 menu choice
    issue_rating_counter()

elif main_menu == 3:  # added new selection for task 2 menu choice
    parcels_effected()

else:
    print('This part of the program is still under development')
