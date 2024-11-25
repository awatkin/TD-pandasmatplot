import pandas as pd
import matplotlib.pyplot as plt  # added new import to bring graphing library in.


# Outputs the initial menu and checks validates the input
def main_menu():
    flag = True

    while flag:

        print("####################################################")
        print("##############   Versere Cars Menu    ##############")
        print("####################################################")
        print("")
        print("########### Please select an option ################")
        print("### 1. Total sales income from different models")
        print("### 2. Problem 1 Sales over time for a specific sales person")  # New menu option added for task 1.
        print("### 3. Problem 1a Total sales for each salesperson")  # New menu option added for task 1a.
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


# Submenu for totals, provides type check validation for the input
def total_menu():
    flag = True

    while flag:

        print("####################################################")
        print("############## Total income by Model ##############")
        print("####################################################")
        print("")
        print("########## Please select an income source ##########")
        print("### 1. Ranger")
        print("### 2. Model D Premium Plus")
        print("### 3. Compass")
        print("### 4. Mercury")
        print("### 5. Ranger")
        print("### 6. Outback")

        choice = input('Enter your number selction here: ')

        try:
            int(choice)
        except:
            print("Sorry, you did not enter a valid option")
            flag = True
        else:
            print('Choice accepted!')
            flag = False

    return choice


# takes the total submenu input and converts the number to a string of the source name
def convert_total_men_choice(total_men_choice):
    if total_men_choice == "1":
        tot_choice = "Ranger"
    elif total_men_choice == "2":
        tot_choice = "Model D Premium Plus"
    elif total_men_choice == "3":
        tot_choice = "Compass"
    elif total_men_choice == "4":
        tot_choice = "Mercury"
    elif total_men_choice == "5":
        tot_choice = "Ranger"
    else:
        tot_choice = "Outback"

    return tot_choice


# new subroutine for sales peron over time problem 1
def sales_person_overtime(sales_person_c):
    df = pd.read_csv("Task3_data.csv")  # reads in the dataframe (fresh and clean)
    if sales_person_c == "1":  # conditional statement to select the sales person, to stop input error
        spc = "Christopher Clark"
    elif sales_person_c == "2":
        spc = "Michael Garcia"
    elif sales_person_c == "3":
        spc = "David Johnson"
    elif sales_person_c == "4":
        spc = "Sarah Jones"

    df1 = df[(df['Salesperson']==spc)]  # slices the df to only show our selected salesperson
    print("The sales over time for ", spc, " :")  # nice message before printing out.
    print(df1)  # print out the data for chosen sales person over time, problem 1 complete.
    print("")
    print("")
    graphdf = df1[['Date','Value']]  # strips dataset down to just data and value.
    graphdf.set_index('Date', inplace=True)  # sets the date to be index so that dates show on graph with sales for each date.
    title = spc, ": Individual sales totals"  # concat for title of chart
    graphdf.plot.bar()  # plot figures as a bar chart
    plt.title(title)  # set title
    plt.show()  # show the graph
    print("The total sales for ", spc, " are:")
    df1 = df1['Value'].sum()  # calculate total sales for that sales person.
    print(df1)


# new subroutine to work out which of the sales people you want to view.
def sales_person_menu():
    flag = True  # sets a check flag to help with input validation

    while flag:  # starts the while loop with the flag

        print("####################################################")
        print("############## Sales Person Selector  ##############")
        print("####################################################")
        print("")
        print("########## Please select an income source ##########")
        print("### 1. Christopher Clark")
        print("### 2. Michael Garcia")
        print("### 3. David Johnson")
        print("### 4. Sarah Jones")

        choice = input('Enter your number selction here: ')  # Captures user input of number

        try:
            int(choice)  # try to int it, ensure its a number
        except:
            print("Sorry, you did not enter a valid option")  # if not, error messages
            flag = True  # set flag to loop again
        else:
            print('Choice accepted!')  # accept and move on
            flag = False

    return choice  # return the number they chose when correct.


# new subroutine to solve problem 1a, total for each sales person
def salesperson_indi_totals():  # declartion of the new subroutine
    df = pd.read_csv("Task3_data.csv")  # Read in fresh clean dataframe
    df1 = df[['Value','Salesperson']]  # slices away unneeded columns
    df1 = df1.groupby('Salesperson').sum()  # sums the data for each salesperson
    print("The total sales for each individual salesperson is :")
    print(df1)  # prints out the data for the user.
    df1.plot.bar()
    plt.title("Sales Person Individual sales totals")
    plt.show()


# creates a new dataframe with the selected income source then creates a total row
# outputs the final total in a message
def get_total_data(total_choice):
    df = pd.read_csv("Task3_data.csv")

    income = df[df["Car Model"]==total_choice]
    total = income[["Value"]].sum().sum()

    msg = "The total income from {} was: £{}".format(total_choice, total)
    return msg


main_menu_choice = main_menu()
if main_menu_choice == "1":
    total_men_choice = total_menu()
    total_choice = convert_total_men_choice(total_men_choice)
    print(get_total_data(total_choice))
elif main_menu_choice == "2":  # new condition on selection statement for Problem 1.
    sales_person_choice = sales_person_menu()  # calls a subroutine to find the sales person
    sales_person_overtime(sales_person_choice)
elif main_menu_choice == "3":  # new condition on selection statement for Problem 1.
    salesperson_indi_totals()

