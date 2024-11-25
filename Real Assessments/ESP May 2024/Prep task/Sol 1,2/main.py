import pandas as pd
import matplotlib.pyplot as plt  # Needed import using standard plt format


''' Tasks to be completed
The solution must also identify trends and patterns over a period of time for:

Completed in this code: The Total sales for each Revenue Streams
Completed in this code: The average sales for AM vs PM for a selected Revenue Stream
The sales of a selected Revenue stream over a period of days selected by the user
A comparison of AM sales Vs PM sales combining all revenue streams.'''


#  solution 1 and 2  below to give totals for each rev stream


def getdf():  # new subroutine to import a clean dataframe and return it.
    df = pd.read_csv("Task4_tester.csv")  # reads in the csv using pandas into a dataframe
    return df  # sends the dataframe back to the calling subroutine.


def amvspmsales():  # new subroutine to solve task 2
    df = getdf()  # gets in a clean dataframe
    revstream = get_revstream_choice()  # gets the users revenue stream choice
    df1 = df[['Time', revstream]]  # takes just Time and the selected revstream forward
    df1 = df1.groupby('Time').mean()  # uses groupby and mean() to provide the average
    df1.plot.bar()  # sends dataseries to maptlotlib as bar chart
    plt.title("Average sales for AM vs PM")  # Sets the title of the chart
    plt.show()  # makes the chart show to the user
    return df1  # returns the needed data series


def revstreamtotals():  # Added a new subroutine (at the top) to get totals
    df = getdf()  # This calls the new subroutine above to get a clean dataframe
    df1 = df[['Tickets', 'Gift Shop', 'Snack Stand', 'Pictures']]  # Copies only needed columns from df to the new df1
    df1 = df1.sum()  # This runs a sum function on each column and makes it into a series
    df1.plot()  # sends the dataseries to matplotlib
    plt.title("Sol 1: Revenue Stream Totals")  # Sets the title of the chart
    plt.show()  # Triggers the chart to be shown to the user
    return df1  # This returns the calculated series


# Displays the main menu and collects choice of menu item


def menu():

    flag = True

    while flag:
        print("###############################################")
        print("Welcome! Please choose an option from the list")
        print("1. Show sales for a specific Revenue Stream")
        print("2. Show total sales for each revenue stream")  # Added a new menu option for solution 1
        print("3. Average sales for AM vs PM for a selected Revenue Stream")  # Added a new menu option for solution 2

        main_menu_choice = input("Please enter the number of your choice (1-3): ")  # Adjusted text for more options

        try:
            int(main_menu_choice)
        except Exception as e:
            print("Sorry, you did not enter a valid choice")
            print("You generated the following error: ", e)
            flag = True
        else:
            if int(main_menu_choice) < 1 or int(main_menu_choice) > 3:  # changed 2 to 3 for option choices
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

elif main_menu == 2:  # New menu item checked for - solution 1
    totals = revstreamtotals()  # captures the returned dataframe / series to print
    print("Here is the total sales for each revenue stream:")  # Pre-cursor message for usability
    print(totals)  # Prints out the returned data series
elif main_menu == 3:  # New menu item checked for - solution 2
    totals = amvspmsales()  # captures the returned results
    print("Here is the average AM vs PM sales for a selected revenue stream:")  # message for readability
    print(totals)  # prints out the returned data
else:
    print('This part of the program is still under development')
