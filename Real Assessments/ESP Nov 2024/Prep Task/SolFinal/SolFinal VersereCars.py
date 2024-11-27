import pandas as pd
import matplotlib.pyplot as plt  # added new import to bring graphing library in.


# new subroutine for robustness as this is used alot, so made it its own subroutine.
def getdf():
    df = pd.read_csv("Task3_data.csv")
    return df

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
        print("### 8. Problem 4 Brand sales over a period of time")
        print("### 9. Problem 4a Model sales over a period of time")  # new menu option for problem 3a
        print("### 10. Quit")

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

def total_brand_menu():
    flag = True

    while flag:

        print("####################################################")
        print("################## Brand Selector ##################")
        print("####################################################")
        print("")
        print("########## Please select an income source ##########")
        print("### 1. Ford")
        print("### 2. Jeep")
        print("### 3. Tesla")
        print("### 4. Subaru")

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
    df = getdf()  # reads in the dataframe (fresh and clean), returned from subroutine
    if sales_person_c == "1":  # conditional statement to select the sales person, to stop input error
        spc = "Christopher Clark"
    elif sales_person_c == "2":
        spc = "Michael Garcia"
    elif sales_person_c == "3":
        spc = "David Johnson"
    elif sales_person_c == "4":
        spc = "Sarah Jones"

    df1 = df[(df['Salesperson'] == spc)]  # slices the df to only show our selected salesperson
    print("The sales over time for ", spc, " :")  # nice message before printing out.
    print(df1)  # print out the data for chosen sales person over time, problem 1 complete.
    print("")
    print("")
    graphdf = df1[['Date', 'Value']]  # strips dataset down to just data and value.
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
    df = getdf()  # Read in fresh clean dataframe, returned from subroutine
    df1 = df[['Value', 'Salesperson']]  # slices away unneeded columns
    df1 = df1.groupby('Salesperson').sum()  # sums the data for each salesperson
    print("The total sales for each individual salesperson is :")
    print(df1)  # prints out the data for the user.
    df1.plot.bar()
    plt.title("Sales Person Individual sales totals")
    plt.show()


# new subroutine for total brand sales to solve problem 2
def total_brand_sales():
    df = getdf()  # read in the fresh new dataframe, returned from subroutine

    df1 = df[['Brand', 'Value']]  # removes unneeded columns of data
    df1 = df1.groupby('Brand').sum()  # totals the sles for each of the brands

    print("The total sales for each brand is :")
    print(df1)  # prints out the data for the user.

    df1.plot.bar()  # plots the data as a chart
    plt.title("Total sales for each brand")  # sets the plt title
    plt.show()  # shows the chart.


def total_model_sales():
    df = getdf()  # read in the fresh new dataframe, returned from subroutine

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
    df = getdf() # gets fresh clean df, returned from subroutine.
    brands = get_brands()  # calls get brands to find out the brans they want to look at.
    df1 = df[['Brand', 'Value']]  # filters down to just brand and value
    df1 = df1[df1['Brand'].isin(brands)]  # uses the list of brands to filter down to those brands only
    df1 = df1.groupby('Brand').sum()  # groups the data and totals it up per brand.
    print(df1)  # prints out the results
    df1.plot.bar()  # sends the results to plot in a bar chart
    plt.title("Brands compared over time")  # sets chart title
    plt.show()  # shows the chart, once quit, return to menu


# new subroutine for getting the selected models
def get_models():
    models = []  # empty list to hold the selected models
    flag = True  # flag for loop

    while flag:
        print("####################################################")
        print("################## Model Selector ##################")
        print("####################################################")
        print("")
        print("########## Please select a Model ##########")
        if "Ranger" not in models:  # checks if they have already chosen this model
            print("### 1. Ranger")  # if not prints the option out.
        if "Model D Premium Plus" not in models:  # checks if they have already chosen this model
            print("### 2. Model D Premium Plus")  # prints it if not
        if "Compass" not in models:
            print("### 3. Compass")
        if "Mercury" not in models:
            print("### 4. Mercury")
        if "Outback" not in models:
            print("### 5. Outback")
        print("### 7. Done")

        print("Currently in your Models list is : ", models)  # feeds back what they have already chosen.

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


# new subroutine to solve problem 4
def brand_sales_overtime():
    df = getdf()  # gets a fresh df from the subroutine for it.
    brand = total_brand_menu()  # gets the brands that user selected
    brandchoice = ""  # declares an empty variable to store the string wanted
    if brand == "1":
        brandchoice = "Ford"
    if brand == "2":
        brandchoice = "Jeep"
    if brand == "3":
            brandchoice = "Tesla"
    if brand == "4":
            brandchoice = "Subaru"

    df1 = df[['Date', 'Brand', 'Value']]  # filters the df down to the needed fields only
    df1 = df1[df1['Brand'] == brandchoice]  # filters it further to just be the brand chosen
    df1 = df[['Date', 'Value']]  # further filtering to get just the date and value for set brand.
    df1.set_index('Date', inplace=True)  # sets an index for the date to make it easier to plot
    df1.plot.bar()  # plots the data
    title = brandchoice + " Sales over time"  # sets a string for the title
    plt.title(title)
    plt.show()


# new subroutine to solve problem 4a
def model_sales_overtime():
    df = getdf()  # gets a fresh df from the subroutine for it.
    model = total_menu()  # gets the choice of model the user wants
    modelchoice = ""  # fresh variable for the model choice string
    if model == "1":
        modelchoice = "Ford"
    if model == "2":
        modelchoice = "Jeep"
    if model == "3":
        modelchoice = "Tesla"
    if model == "4":
        modelchoice = "Subaru"

    df1 = df[['Date', 'Car Model', 'Value']]  # filters down the data to needed fields.
    df1 = df1[df1['Car Model'] == modelchoice]  # filters based on user choice of model
    df1 = df[['Date', 'Value']]  # removes the now not needed model field
    df1.set_index('Date', inplace=True)  # sets the index to use the date for the graph
    df1.plot.bar()
    title = modelchoice + " Sales over time"
    plt.title(title)
    plt.show()


# new subroutines to solve problem 3a
def compare_model_total_sales():
    df = getdf()  # gets a fresh df from the subroutine for it.
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
    df = getdf()  # gets a fresh df from the subroutine for it.
    income = df[df["Car Model"] == total_choice]
    total = income[["Value"]].sum().sum()

    msg = "The total income from {} was: £{}".format(total_choice, total)
    return msg


#declared a main, standardised way of declaring and running code
def main():
    flag = True
    while flag:
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
        elif main_menu_choice == "8":  # new condition on selection statement for Problem 3.
            brand_sales_overtime()
        elif main_menu_choice == "9":  # new condition on selection statement for Problem 3.
            model_sales_overtime()
        elif main_menu_choice == "10":
            print("Thank you for using the system")
            quit()


# proper way to launch the main subroutine
if __name__ == "__main__":
    main()

