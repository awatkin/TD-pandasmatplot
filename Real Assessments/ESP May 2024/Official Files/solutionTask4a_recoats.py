import pandas as pd  # Imports the pandas library to work with dataframes
import matplotlib.pyplot as plt  # Imports matplotlib to produce graphs where needed


# new subroutine for one central point of reading in a csv to enable readability and error handling.
def df_reader():
    df = pd.read_csv("Task4a_data.csv")  # lifted from get total data so to keep it in one place.

    return df  # returns the fresh clean dataframe.


# Outputs the initial menu and checks validates the input
def main_menu():
    flag = True

    while flag:

        print("####################################################")
        print("############## Recoats Adventure Park ##############")
        print("####################################################")
        print("")
        print("########### Please select an option ################")
        print("### 1. Total income by source")
        print("### 2. Income by payment type")  # added second option to look at payment types
        print("### 3. Total income by payment type and sources")  # added third option for pay types and income sources
        print("### 4. Total income by day of the week")  # added fourth option to look at pay on each day
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
        print("############## Total income by source ##############")
        print("####################################################")
        print("")
        print("########## Please select an income source ##########")
        print("### 1. Tickets")
        print("### 2. Gift Shop")
        print("### 3. Snack Stand")
        print("### 4. Pictures")

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


# new subroutine to get payment type wanted
def payment_type():
    flag = True

    while flag:
        print("####################################################")
        print("############## Income by payment type ##############")
        print("####################################################")
        print("")
        print("########## Please select an income source ##########")
        print("### 1. Cash")
        print("### 2. Card")
        print("### 3. Both")


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
def convert_total_men_coice(total_men_choice):
    if total_men_choice == "1":
        tot_choice = "Tickets"
    elif total_men_choice == "2":
        tot_choice = "Gift Shop"
    elif total_men_choice == "3":
        tot_choice = "Snack Stand"
    else:
        tot_choice = "Pictures"

    return tot_choice


# creates a new dataframe with the selected income source then creates a total row
# outputs the final total in a message
def get_total_data(total_choice):

    df = df_reader()  # new line, gets a fresh data frame from the new subroutine.

    income = df[["Day", total_choice]]

    total = income[total_choice].sum()

    msg = "The total income from {} was: £{}".format(total_choice, total)
    return msg


# new subroutine to total cash sales for each stream
def cash_total():
    df = df_reader()  # gets a fresh clean dataframe

    ''' This section works out cash sales by each of the revenue streams and outputs a graph'''

    df1 = df.groupby('Pay Type')[['Tickets','Gift Shop','Snack Stand','Pictures']].sum()  # this groups by pay type, then totals the sales for each rev stream
    print("The total sales in Cash for each revenue source:")
    df2 = df1.loc['Cash']  # just focuses on the cash
    print(df2)
    df2.plot.bar()  # uses df1 for a bar chart
    plt.title("Cash across revenue streams")  # sets the title
    plt.show()  # shows the chart

    ''' This section works out cash sales by each day of the week and outputs a graph'''

    df1 = df.groupby(['Day','Pay Type']).sum().sum(axis=1)  # this groups by pay type, then totals the sales for each rev stream
    print("The total sales in Cash for each day:")
    df2 = df1[df1.index.get_level_values('Pay Type') == 'Cash']  # splits out and hides the card payment element
    print(df2)
    df2.plot.bar()  # uses df1 for a bar chart
    plt.title("Cash across Days")  # sets the title
    plt.show()

    ''' This section works out the total cash sales combined into one value'''

    df1 = df.groupby('Pay Type')[['Tickets','Gift Shop','Snack Stand','Pictures']].sum().sum(axis=1)  # totals cash and sales, removes the days

    print("The total sales for Cash is:")
    print(df1.loc['Cash'])


#new subroutine for card payments
def card_total():
    df = df_reader()  # gets a fresh clean dataframe

    ''' This section works out card sales by each of the revenue streams and outputs a graph'''

    df1 = df.groupby('Pay Type')[['Tickets','Gift Shop','Snack Stand','Pictures']].sum()  # this groups by pay type, then totals the sales for each rev stream
    print("The total sales in Card for each revenue source:")
    df2 = df1.loc['Card']  # just focuses on the cash
    print(df2)
    df2.plot.bar()  # uses df1 for a bar chart
    plt.title("Card across revenue streams")  # sets the title
    plt.show()  # shows the chart

    ''' This section works out card sales by each day of the week and outputs a graph'''

    df1 = df.groupby(['Day','Pay Type']).sum().sum(axis=1)  # this groups by pay type, then totals the sales for each rev stream
    print("The total sales in Card for each day:")
    df2 = df1[df1.index.get_level_values('Pay Type') == 'Card']  # splits out and hides the card payment element
    print(df2)
    df2.plot.bar()  # uses df1 for a bar chart
    plt.title("Cardacross Days")  # sets the title
    plt.show()

    ''' This section works out the total card sales combined into one value'''

    df1 = df.groupby('Pay Type')[['Tickets','Gift Shop','Snack Stand','Pictures']].sum().sum(axis=1)  # totals cash and sales, removes the days

    print("The total sales for Cash is:")
    print(df1.loc['Card'])


# new subroutine to show both rev sources against each other
def both_total():
    df = df_reader()  # gets a fresh clean dataframe

    ''' This section works out sales by each of the revenue streams and outputs a graph'''

    df1 = df.groupby('Pay Type')[['Tickets','Gift Shop','Snack Stand','Pictures']].sum()  # this groups by pay type, then totals the sales for each rev stream
    print("The total sales in Card for each revenue source:")
    print(df1)
    df1.plot.bar()  # uses df1 for a bar chart
    plt.title("Revenue revenue streams")  # sets the title
    plt.show()  # shows the chart

    ''' This section works out cash sales by each day of the week and outputs a graph'''

    df1 = df.groupby(['Day','Pay Type']).sum().sum(axis=1)  # this groups by pay type, then totals the sales for each rev stream
    print("The total sales in Card for each day:")
    print(df1)
    df1.plot.bar()  # uses df1 for a bar chart
    plt.title("Payment across Days")  # sets the title
    plt.show()

    ''' This section works out the total cash sales combined into one value'''

    df1 = df.groupby('Pay Type')[['Tickets','Gift Shop','Snack Stand','Pictures']].sum().sum(axis=1)  # totals cash and sales, removes the days

    print("The total sales for Cash is:")
    print(df1)


# new subroutine to calculate the totals for each payment type
def payment_type_total():
    choice = payment_type()

    if choice == "1":
        cash_total()
    elif choice == "2":
        card_total()
    elif choice == "3":
        both_total()


# all code, as accepted convention, should be launched from a main()
def main():

    flag = True  # sets a flag to keep system going until exited

    while flag:  # establishes a while loop to keep system going
        main_menu_choice = main_menu()
        if main_menu_choice == "1":
            total_men_choice = total_menu()
            total_choice = convert_total_men_coice(total_men_choice)
            print(get_total_data(total_choice))
        elif main_menu_choice == "2":
            payment_type_total()
        elif main_menu_choice == "3":
            pass
        elif main_menu_choice == "4":
            pass
        elif main_menu_choice == "7":
            print("Thanks for using the system")
            quit()


# accepted convention to launch code
if __name__ == "__main__":
    main()
