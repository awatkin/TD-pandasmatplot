import pandas as pd  # standard naming convention for pandas
import matplotlib.pyplot as plt  # standard naming convention for plotlib

'''Below is the read_data function, this is callable, reads in a fresh copy of the csv file
returns a dataframe for you to capture into a variable.'''


def read_data():  # define the subroutine
    df = pd.read_csv('Task4a_data.csv')  # uses pandas function to read in the csv in df variable
    return df  # returns the dataframe to where it was requested


'''This below function will take the fresh dataframe and 
print out the contents for the user, but cut down as that is default'''


def read_all_data():  # this sub routine will read in a fresh csv file and print out the entire contents
    df = read_data()  # capture the dataframe, fresh one, from read_data into a variable.
    print(df)  # print out the data, will be cut down for clarity in the console.


''' The below subroutine WILL take in the data, allow the user
to select the food item they want and show a graph for the
food item cross both services that it is available for.
This is to show how to wrangle data AND show how to set
series names when they have come from a dataframe like this'''


def food_service_graph():  # starts new subroutine to build a graph about item sales.
    df = read_data()  # gets a fresh dataframe in to work with.
    print(df)


'''The below subroutine takes in a fresh dataframe and then
strips out the service to run a total and then outputs
this data via the console and a matplot lib bar chart'''


def total_each_item():  # This sub routine will calculate the totals for each menu item and print them with a graph
    df = read_data()  # calls the read in function to get a fresh dataframe, which is good security.

    df1 = df.drop(['Service'], axis=1)  # this drops the Service column and its data as not needed for this

    df1 = df1.groupby('Menu Item').sum().sum(axis=1)  # runs a sum and averages with "mean()" function

    print(df1)  # print out the averages

    df1.plot.bar()  # sends the data to a plot, specifically a bar chart
    plt.title("Total Sales for Each Menu Item, across both Services")  # sets the title of the chart
    plt.show()  # triggers the showing of the plot to the user.


'''The below subroutine takes in a fresh dataframe and then
strips out the service to run a mean / average and then outputs
this data via the console and a matplot lib bar chart'''


def average_each_item():  # This sub does similar to totals, but average instead
    df = read_data()  # Creates a fresh, secure, data frame

    df1 = df.drop(['Service'], axis=1)  # drops the service column again as not needed
    df1 = df1.groupby('Menu Item').sum().mean(axis=1)  # groups data and runs sum and average / mean

    print(df1)  # prints the averages out

    print("The item with the highest average is: ", df1.idxmax())  # makes use of idxmax to give the top average item

    df1.plot.bar()  # Sends data to matplotlib as a bar chart
    plt.title("Average of Each menu item sales")  # sets the title
    plt.show()  # shows the chart


def main():
    flag = True
    while flag:
        print("Welcome to the T-level Digital Python helper, choose an option to see the output.")
        print("")
        print("")
        print("[1] Read in data frame and print out the data")
        print("[2] Read in Data, strip down to show one food type on both services")
        print("[3] Count the number of times each menu item appears in the dataframe")
        print("[4] Calculate the total number of sales for each menu item")
        print("[5] Calculate the average number of sales across the time period")
        print("[6] quit")
        print("")
        print("Enter your choice to run the code")
        choice = str(input("Enter your choice: "))
        if choice == "1":
            read_all_data()
        if choice == "4":
            total_each_item()
        if choice == "5":
            average_each_item()
        elif choice == "6":
            flag = False
            print("Thank you for using T-level Digital Python helper!")
        else:
            print("Enter a choice that is valid")


''' industry standard way of launching code:
You should use a main() to start things, and to launch the main
you should have the line of code below. This also helps with maintainability,
security and generally good coding. '''

if __name__ == '__main__':  # standard (good) way to launch you main
    main()
