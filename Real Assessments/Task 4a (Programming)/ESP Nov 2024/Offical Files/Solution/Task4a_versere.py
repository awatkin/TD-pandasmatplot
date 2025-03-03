import pandas as pd
import matplotlib.pyplot as plt  # added a new import for the graphing library


def getdf():  # new sub routine as the df will be read in multiple times.
    df = pd.read_csv("Task4a_data.csv")  # reads in the csv file into a dataframe using pandas
    return df


# new subroutine for total sales for new and used cars
def total_sales_newused():
    df = getdf()  # gets the dataframe in from the subroutine
    df = df[['New/Used', 'Value']]
    df = df.groupby('New/Used').sum()
    print("The total sales for new and used cars is:")
    print(df)
    df.plot.bar()  # sets the df to be a bar chart via mat plot lib
    plt.title("Total Sales of New and Used Cars")   # sets the title of the graph
    plt.show()  # shows it and awaits being closed before moving on.


# new subroutiune to run menu option 3 newused sales over time
def newused_overtime():
    df = getdf()  # gets a fresh clean dataset in, as data may have been updated.
    flag = True

    while flag:  # menu to get the users wanted output
        print("#################################################")
        print("############## New Used Overtime ##############")
        print("#################################################")
        print("")
        print("########### Please select an option #############")
        print("### 1. Used sales over time")
        print("### 2. New Sales over time")
        print("### 3. New and Used Sales over time")
        print("")
        choice = input('Enter your number selection here: ')  # captures the input from user

        try:  # trys to int it to ensure number was entered
            int(choice)
        except:
            print("Sorry, you did not enter a valid option")
            flag = True
        else:
            print('Choice accepted!')
            flag = False  # used to exit the loop if a suitable int is used.

    if choice == "1" or choice == "2":  # if choice is new or used
        if choice == "1":
            newused = "Used"  # sets a variable according to choice
        else:
            newused = "New"
        df1 = df[df['New/Used'] == newused]  # filters the data to just the new or used data
        df1 = df1[['Date', 'Value']]  # filters down the frame to needed columns

        df1 = df1.groupby('Date')['Value'].sum()  #  groups by the date and then totals the value for each date#
        print(" The ", newused, " sales over time is: ")
        print(df1)  # prints out the data to view
        title = newused + " sales over time"  # sets chart title for this data
        df1.plot.bar()  # sets it to be a bar chart
        plt.title(title)  # sets the title using the variable
        plt.show()  # shows the grpah

    elif choice == "3":
        #df1 = df[df['New/Used'] == newused]  # filters the data to just the new or used data
        df1 = df[['Date', 'New/Used', 'Value']]  # filters down the frame to needed columns

        df1 = df1.groupby(['Date', 'New/Used'])['Value'].sum()  # groups by the date and then totals the value for each date#
        print(" The New and Used sales over time is: ")
        print(df1)  # prints out the data to view
        title = "New and Used sales over time"  # sets chart title for this data
        df1.plot.bar()  # sets it to be a bar chart
        plt.title(title)  # sets the title using the variable
        plt.show()  # shows the graph


# new subroutine for staff total sales
def staff_totalsales():
    df = getdf()  # brings in a new fresh

    df1 = df[['Value', 'Salesperson']]
    df1 = df1.groupby('Salesperson').sum()
    print("The total sales for each salesperson is:")
    print(df1)
    df1.plot.bar()
    plt.title("Total Sales per Salesperson")
    plt.show()


def get_staff():
    staff = []
    flag = True

    while flag:
        print("####################################################")
        print("################## Staff Selector ##################")
        print("####################################################")
        print("")
        print("########## Please select a Model ##########")
        if "Christopher Clark" not in staff:
            print("### 1. Christopher Clark")
        if "Michael Garcia" not in staff:
            print("### 2. Michael Garcia")
        if "David Johnson" not in staff:
            print("### 3. David Johnson")
        if "Sarah Jones" not in staff:
            print("### 4. Sarah Jones")
        print("### 7. Done")

        print("Currently in your Models list is : ", staff)

        choice = input('Enter your number selction here: ')  # Captures user input of number

        try:
            int(choice)  # try to int it, ensure its a number
        except:
            print("Sorry, you did not enter a valid option")  # if not, error messages
            flag = True  # set flag to loop again
        else:
            if choice == "1":
                if "Christopher Clark" not in staff:  # checks ford hasn't been put in already
                    staff.append("Christopher Clark")  # if not already in there appends them to the list
            elif choice == "2":
                if "Michael Garcia" not in staff:  # checks Subaru hasn't been put in already
                    staff.append("Michael Garcia")
            elif choice == "3":
                if "David Johnson" not in staff:  # checks Jeep hasn't been put in already
                    staff.append("David Johnson")
            elif choice == "4":
                if "Sarah Jones" not in staff:  # checks Tesla hasn't been put in already
                    staff.append("Sarah Jones")
            elif choice == "7":  # if selected "Done"
                if len(staff) > 1:  # makes sure they have made a choice to complete
                    flag = False
                else:
                    print("Not enough choices made, please pick some brands")

            print('Choice accepted!')  # accept and move on

    return staff

# new subroutine to show staff over time.
def staff_overtime():
    df = getdf()  # imports fresh data set
    staff = get_staff()  # collects the staff that wish to be compared
    df1 = df[df['Salesperson'].isin(staff)]  # uses the list of brands to filter down to those brands only
    df1 = df1[['Date', 'Value', 'Salesperson']]  # filters down to just brand and value
    df1 = df1.groupby(['Date', 'Salesperson']).sum()  # groups the data and totals it for each brand
    print(df1)  # prints out the facts
    df1_unstacked = df1.unstack()
    df1_unstacked.plot.bar()  # plots to a bar chart
    plt.xlabel("Date")
    plt.ylabel("Total Value")
    plt.title("Models compared over time")  # Sets title for the charts
    plt.show()  # shows the chart
# subroutine for the main menu
def main_menu():
    flag = True

    while flag:

        print("#################################################")
        print("############## Versere Cars Sales ##############")
        print("#################################################")
        print("")
        print("########### Please select an option #############")
        print("### 1. Total Sales Analysis")
        print("### 2. Total sales for new and used cars")  # new option for total sales of new and used
        print("### 3. New and Used car sales over time ")
        print("### 4. Total sales per salesperson ")
        print("### 5. Sales over time for sales people ")
        print("### 7. Quit ")  # new option to quit the system when done.

        choice = input('Enter your number selection here: ')

        try:
            int(choice)
        except:
            print("Sorry, you did not enter a valid option")
            flag = True
        else:    
            print('Choice accepted!')
            flag = False

    return choice


def total_menu():
    flag = True

    while flag:

        print("#################################################")
        print("############## Total Sales ##############")
        print("#################################################")
        print("")
        print("########### Please select an option #############")
        print("### 1. All sales by model")   
        print("### 2. Custom selection") 

        choice = input('Enter your number selection here: ')

        try:
            int(choice)
        except:
            print("Sorry, you did not enter a valid option")
            flag = True
        else:    
            print('Choice accepted!')
            flag = False

    return choice      


def convert_total_menu_coice(total_menu_choice):
    
    if total_menu_choice == "1":
        total_choice = "All"
    else:
        total_choice = "Model"  
    
    return total_choice


def get_total_data(total_choice):
    
    df = getdf()

    if total_choice == "All":
        extract = df.groupby(['Date', 'Car Model'], sort=True)['Value'].sum()
        total = df['Value'].sum()
        print("The total value of sales for your selection is {}".format(total))

    else:
        flag = True

        while flag:

            print("########### Please select a model #############")
            print("### 1. Ranger")
            print("### 2. Model D Premium Plus")
            print("### 3. Compass")
            print("### 4. Mercury")
            print("### 5. Outback")
            
            choice = input('Enter your number selection here: ')

            try:
                int(choice)
            except:
                print("Sorry, you did not enter a valid option")
                flag = True
            else:    
                print('Choice accepted!')
                choice = int(choice)
                flag = False

        models = ["Ranger", "Model D Premium Plus", "Compass", "Mercury", "Outback"]   

        custom_choice = models[choice - 1]

        extract = df.loc[df['Car Model'] == custom_choice]
        total = extract['Value'].sum()
        print("The total value of sales for your selection is {}".format(total))

    return extract


# new main subroutine to allow looping and do things proper way.
def main():
    flag = True

    while flag:  # triggers a loop on the flag to allow it to keep looping until the user exits.

        main_menu_choice = main_menu()

        if main_menu_choice == "1":
            total_menu_choice = total_menu()
            total_choice = convert_total_menu_coice(total_menu_choice)
            print(get_total_data(total_choice))
        elif main_menu_choice == "2":  # added a menu choice for new / used car sales
            total_sales_newused()
        elif main_menu_choice == "3":  # added a menu choice for new / used car sales over time
            newused_overtime()  # calls the appropraite sub routine to run this option
        elif main_menu_choice == "4":  # added a menu choice for new / used car sales over time
            staff_totalsales()  # calls the appropraite sub routine to run this option
        elif main_menu_choice == "5":  # added a menu choice for new / used car sales over time
            staff_overtime()  # calls the appropraite sub routine to run this option
        elif main_menu_choice == "7":  # added a menu choice to quit
            print("Thank you for using the system")  # message output before quitting#
            quit()  # stops the code running safely.
        else:
            print("This section is under construction")


# for robustness and correctness, this is how a main should be launched
if __name__ == "__main__":
    main()
