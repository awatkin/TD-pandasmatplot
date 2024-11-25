import pandas as pd

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
        print("### 2. Sales over time for a specific sales person")  # New menu option added for task 1.

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
elif main_menu_choice == "2":
    pass
