import pandas as pd
import matplotlib.pyplot as plt  # Added This import to allow use of graphing


# This is the solution to Task 1, Task 2, Task 3 ,Task 4 and has robustness built int
# The tasks are:
# Task 1 - The total number of each issue type and the average rating for that problem
# Task 2 - The Number of Parcels effected for each Issue Type
# Task 3 - The Number of issues for each region
# Task 4 - A crosstab of Parcels effected vs the Rating given
# All changes have comments on / around them to show them


def read_df():  # new subroutiner to read in fresh df, centralise maintenance
    df = pd.read_csv("May25_prepdata.csv")
    return df


# Displays the main menu and collects choice of menu item
def menu():
    flag = True

    while flag:
        print("######################Bode Parcels#########################")
        print("Welcome! Please choose an option from the list")
        print("1. Show Data for one issue")
        print("2. Issue Numbers and rating (TASK 1)")  # updated this line to accomodate task 1 option
        print("3. No, Of Parcels for each issue (TASK 2)")  # added a new entry for task 2 selection
        print("4. No, Of Issues for each Region (TASK 3)")  # added a new entry for task 3 selection
        print("5. Cross Tab of No of Parcels vs Ratings (TASK 4)")  # added a new entry for task 4 selection
        print("")
        print("")
        print("6. QUIT")  # added a new entry to allow quitting

        main_menu_choice = input("Please enter the number of your choice (1-6): ")  # updated this line to accomodate further than option 2

        try:
            int(main_menu_choice)
        except Exception as e:
            print("Sorry, you did not enter a valid choice")
            print("You generated the following error: ", e)
            flag = True
        else:
            if int(main_menu_choice) < 1 or int(main_menu_choice) > 6:  # further updated this to allow higher than 2
                print("Sorry, you did not enter a valid choice")
                flag = True
            else:
                return int(main_menu_choice)

            # Menu item selection form user and validates it


def bar_grapher(data, title):  # added new subroutine to aid maintenance to allow bar graphs from one place.
    data.plot.bar()
    plt.title(title)
    plt.show()


def scatter_grapher(data, title): # added new subroutine to aid maintenance to allow bar graphs from one place.
    data.plot()
    plt.title(title)
    plt.show()

def issues_against_regions():  # New subroutine to solve task 4
    df = read_df()  # read in a fresh clean dataframe
    df = pd.crosstab(df["No Of Parcels"], df["Rating"])

    scatter_grapher(df, "Cross Tab of No of Parcels vs Ratings") # updated line of code to use new subroutine


def region_issue():  # New subroutine to solve task 3
    df = read_df()  # read in a fresh clean dataframe

    issue_count = df[["Region"]].groupby(["Region"]).size()  # this removes unneeded columns, then counts the number of issues for each region
    print(issue_count)  # prints out the results

    # graph out the results

    bar_grapher(issue_count, "Total Issues Per Region")  # updated line of code to use bar graphing routine

def parcels_effected():  # new subroutine to solve task 2
    df = read_df()  # read in a fresh clean dataframe
    effected = df[["Issue Type", "No Of Parcels"]]  # reduces down the df to just needed columns
    effected = effected.groupby(["Issue Type"])["No Of Parcels"].sum()  # this groups by issue type and totals the number of parcels
    print("The Number parcels for each issue Type is: ")
    print(effected)  # this outputs the count of each parcel count type

    bar_grapher(effected, "Total Parcels Per Issue Type")  # updated line to use new grapher routine

def issue_rating_counter():  # added a new subroutine to solve the task 1 problem
    df = read_df()  # read in a fresh clean dataframe

    issue_counts = df[["Issue Type"]].value_counts()  # This reduces the dataframe to just the Issue type column then counts each issue type
    print("The Number of each issue Type is: ")
    print(issue_counts)   # this outputs the count of each issue type

    rating_count = df[["Issue Type", "Rating"]]  # This reduces the df to just the 2 cols needed
    rating_count = rating_count.groupby("Issue Type")  # Then groups the data  by issue type
    rating_count = rating_count["Rating"].mean() # then applies an average to the rating for each issue type.
    print("The average Rating of each issue Type is: ")
    print(rating_count)  # outputs the results.

    # Graphing the data out.
    bar_grapher(issue_counts, "Total Issue Numbers")

    bar_grapher(rating_count, "Rating of Issue Types")


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
    df1 = read_df() # updated life of code to readin fresh df
    df2 = df1[df1["Issue Type"] == item]

    return df2


def main():  # added main as part of the accepted stand conventions for launching code
    flag = True  # added check flag for main loop of main menu
    while flag:  # added while loop to run until user quits

        main_menu = menu()  # calls the main menu to get an option choice

        if main_menu == 1:  # checks the returned value

            issueChoice = get_issue_choice()  # gets their chosen

            extracted_data = get_selected_item(issueChoice)

            print("Here is the sales data for {} :".format(issueChoice))
            print(extracted_data)

        elif main_menu == 2:  # added a new selection statement for task 1 menu choice
            issue_rating_counter()  # calls subroutine to complete task

        elif main_menu == 3:  # added new selection for task 2 menu choice
            parcels_effected()  # calls subroutine to complete task

        elif main_menu == 4:  # added new selection for task 3 menu choice
            region_issue()  # calls subroutine to complete task

        elif main_menu == 5:  # added new selection for task 4 menu choice
            issues_against_regions()  # calls subroutine to complete task

        elif main_menu == 6:  # added new selection for quitting
            quit()  # ends the code running

        else:
            print('Not a valid option')  # updated message to reflect completed code base.


if __name__ == '__main__':  # added the standard convention to launch code
    main()  # launches main on starting up
