import pandas as pd  # imports the pandas library to work with the code
import matplotlib.pyplot as plt  # Needed import using standard plt format


#  This subroutine means that only one place reads in a fresh clean Data frame, not repeated code.
def get_df():
    df = pd.read_csv("Task4a_data.csv")  # open the csv file in the same folder as this pythion, creates df

    return df  # returns the df to the calling sub routine


# Outputs the initial menu and checks validates the input
def main_menu():
    flag = True  # sets a checks flag 

    while flag:

        print("####################################################")
        print("############## Recoats Adventure Park ##############")
        print("####################################################")
        print("")
        print("########### Please select an option ################")
        print("### 1. Total income by source")
        print("### 2. Total income by payment type")
        print("### 3. Total income by payment type AND source")
        print("### 4. Total income by day of the week")
        print("")
        print("")
        print("### 7. Exit")

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


def payment_menu():
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
            if choice == "1":
                tot_choice = "Tickets"
            elif choice == "2":
                tot_choice = "Gift Shop"
            elif choice == "3":
                tot_choice = "Snack Stand"
            else:
                tot_choice = "Pictures"

    return tot_choice


# gets the choice and totals it to output to the user
def get_total_data(total_choice):
    
    df = get_df()  # calls subroutine to get fresh clean dataframe
    income = df[["Day", total_choice]]
    total = income[total_choice].sum()

    msg = "The total income from {} was: £{}".format(total_choice, total)
    return msg


# creates a new dataframe with the selected income source then creates a total row
# outputs the final total in a message
def income_by_source():

    total_choice = payment_menu()
    print(get_total_data(total_choice))  # Prints out the final data for


def income_by_type():
    pass

def main():  # this is the main to loop the programme until it is exited out from.

    flag = True  # sets a flag to keep looping the main menu until

    while flag:

        main_menu_choice = main_menu()
        if main_menu_choice == "1":
            income_by_source()
        elif main_menu_choice == "2":
            pass
        elif main_menu_choice == "3":
            pass
        elif main_menu_choice == "4":
            pass
        elif main_menu_choice == "7":
            print("Thank you for using our system, you will now be logged out")
            quit()


if __name__ == "__main__":  # added condition to start the code, the right way
    main()  # launches main, if the condition is met
