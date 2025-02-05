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
        print("### 4. Problem 2 Show the total sales for each of the Brands")
        print("### 5. Problem 2a Show the total sales for each of the Car Models")
        print("### 6. Problem 3 Compare total sales across brands")
        print("### 7. Problem 3a Compare the total sales of 1 or more models")  # new menu option for problem 3a

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

        choice = input('Enter your number selection here: ')  # Captures user input of number

        try:
            int(choice)  # try to int it, ensure it's a number
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
    df1 = df[['Value', 'Salesperson']]  # slices away unneeded columns
    df1 = df1.groupby('Salesperson').sum()  # sums the data for each salesperson
    print("The total sales for each individual salesperson is :")
    print(df1)  # prints out the data for the user.
    df1.plot.bar()
    plt.title("Sales Person Individual sales totals")
    plt.show()


# new subroutine for total brand sales to solve problem 2
def total_brand_sales():
    df = pd.read_csv("Task3_data.csv")  # read in the fresh new dataframe

    df1 = df[['Brand', 'Value']]  # removes unneeded columns of data
    df1 = df1.groupby('Brand').sum()  # totals the sles for each of the brands

    print("The total sales for each brand is :")
    print(df1)  # prints out the data for the user.

    df1.plot.bar()  # plots the data as a chart
    plt.title("Total sales for each brand")  # sets the plt title
    plt.show()  # shows the chart.


def total_model_sales():
    df = pd.read_csv("Task3_data.csv")  # read in the fresh new dataframe

    df1 = df[['Car Model', 'Value']]  # removes unneeded columns of data
    df1 = df1.groupby('Car Model').sum()  # totals the sles for each of the brands

    print("The total sales for each Model is :")
    print(df1)  # prints out the data for the user.

    df1.plot.bar()  # plots the data to a bar chart
    plt.title("Total sales for each model")  # sets the title
    plt.show()  # displays the chart.


# new subroutine to get brands for problem 3 solution
def get_brands():
    brands = []  # establishes an empty list for the brands to take forward
    flag = True  # sets a check flag to help with input validation

    while flag:  # starts the while loop with the flag

        print("####################################################")
        print("################## Brand Selector  #################")
        print("####################################################")
        print("")
        print("########## Please select the brands you want source ##########")
        if "Ford" not in brands:  # check to see if ford has been selected already
            print("### 1. Ford")
        if "Subaru" not in brands:
            print("### 2. Subaru")
        if "Jeep" not in brands:
            print("### 3. Jeep")
        if "Tesla" not in brands:
            print("### 4. Tesla")
        print("### 7. Done")

        print("Currently in your brands list is : ", brands)

        choice = input('Enter your number selction here: ')  # Captures user input of number

        try:
            int(choice)  # try to int it, ensure its a number
        except:
            print("Sorry, you did not enter a valid option")  # if not, error messages
            flag = True  # set flag to loop again
        else:
            if choice == "1":
                if "Ford" not in brands:  # checks ford hasn't been put in already
                    brands.append("Ford")  # if not already in there appends them to the list
            elif choice == "2":
                if "Subaru" not in brands:  # checks Subaru hasn't been put in already
                    brands.append("Subaru")
            elif choice == "3":
                if "Jeep" not in brands:  # checks Jeep hasn't been put in already
                    brands.append("Jeep")
            elif choice == "4":
                if "Tesla" not in brands:  # checks Tesla hasn't been put in already
                    brands.append("Tesla")
            elif choice == "7":  # if selected "Done"
                if len(brands) > 1:  # makes sure they have made a choice to complete
                    flag = False
                else:
                    print("Not enough choices made, please pick some brands")

            print('Choice accepted!')  # accept and move on

    return brands


# new subroutine to solve problem 3
def compare_brand_total_sales():
    df = pd.read_csv("Task3_data.csv")
    brands = get_brands()
    df1 = df[['Brand', 'Value']]  # filters down to just brand and value
    df1 = df1[df1['Brand'].isin(brands)]  # uses the list of brands to filter down to those brands only
    df1 = df1.groupby('Brand').sum()
    print(df1)
    df1.plot.bar()
    plt.title("Brands compared over time")
    plt.show()


def get_models():
    models = []
    flag = True

    while flag:
        print("####################################################")
        print("################## Model Selector ##################")
        print("####################################################")
        print("")
        print("########## Please select a Model ##########")
        if "Ranger" not in models:
            print("### 1. Ranger")
        if "Model D Premium Plus" not in models:
            print("### 2. Model D Premium Plus")
        if "Compass" not in models:
            print("### 3. Compass")
        if "Mercury" not in models:
            print("### 4. Mercury")
        if "Outback" not in models:
            print("### 5. Outback")
        print("### 7. Done")

        print("Currently in your Models list is : ", models)

        choice = input('Enter your number selction here: ')  # Captures user input of number

        try:
            int(choice)  # try to int it, ensure its a number
        except:
            print("Sorry, you did not enter a valid option")  # if not, error messages
            flag = True  # set flag to loop again
        else:
            if choice == "1":
                if "Ranger" not in models:  # checks ford hasn't been put in already
                    models.append("Ranger")  # if not already in there appends them to the list
            elif choice == "2":
                if "Model D Premium Plus" not in models:  # checks Subaru hasn't been put in already
                    models.append("Model D Premium Plus")
            elif choice == "3":
                if "Compass" not in models:  # checks Jeep hasn't been put in already
                    models.append("Compass")
            elif choice == "4":
                if "Mercury" not in models:  # checks Tesla hasn't been put in already
                    models.append("Mercury")
            elif choice == "5":
                if "Outback" not in models:  # checks Tesla hasn't been put in already
                    models.append("Outback")
            elif choice == "7":  # if selected "Done"
                if len(models) > 1:  # makes sure they have made a choice to complete
                    flag = False
                else:
                    print("Not enough choices made, please pick some brands")

            print('Choice accepted!')  # accept and move on

    return models


# new subroutines to solve problem 3a
def compare_model_total_sales():
    df = pd.read_csv("Task3_data.csv")  # imports fresh data set
    models = get_models()

    df1 = df[['Car Model', 'Value']]  # filters down to just brand and value
    df1 = df1[df1['Car Model'].isin(models)]  # uses the list of brands to filter down to those brands only
    df1 = df1.groupby('Car Model').sum()  # groups the data and totals it for each brand
    print(df1)  # prints out the facts
    df1.plot.bar()  # plots to a bar chart
    plt.title("Models compared over time")  # Sets title for the charts
    plt.show()  # shows the chart


# creates a new dataframe with the selected income source then creates a total row
# outputs the final total in a message
def get_total_data(total_choice):
    df = pd.read_csv("Task3_data.csv")
    income = df[df["Car Model"] == total_choice]
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
elif main_menu_choice == "3":  # new condition on selection statement for Problem 1a.
    salesperson_indi_totals()
elif main_menu_choice == "4":  # new condition on selection statement for Problem 2.
    total_brand_sales()
elif main_menu_choice == "5":  # new condition on selection statement for Problem 2a.
    total_model_sales()
elif main_menu_choice == "6":  # new condition on selection statement for Problem 3.
    compare_brand_total_sales()
elif main_menu_choice == "7":  # new condition on selection statement for Problem 3.
    compare_model_total_sales()


''' tasks to be completed

Problem 4: Show the sales for a Specific Brand over a period of time
Problem 4a: Show the sales for a Specific Model over a period of time. 

'''
