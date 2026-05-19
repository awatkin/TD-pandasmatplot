import pandas as pd
import csv
import matplotlib.pyplot as plt


def read_df():
    df = pd.read_csv("Task4_sample_data.csv", parse_dates=["Date"], dayfirst=True)
    return df


# Outputs the initial menu and validates the input
def main_menu():
    flag = True

    while flag:

        print("####################################################")
        print("############### Glenstar Data System ###############")
        print("####################################################")
        print("")
        print("########### Please select an option ################")
        print("### 1. All Results for one Event type")
        print("### 2. All Results for one Gender - Task 1")
        print("###")
        print("### 15. Quit")

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


# Submenu for gender, provides type check validation for the input and returns event type as a string
def gender_picker():
    flag = True

    while flag:

        print("####################################################")
        print("################## Gender Types ####################")
        print("####################################################")
        print("")
        print("########## Please select an issue type ##########")
        print("### 1. Female")
        print("### 2. Male")

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

    genderList = ["F", "M"]

    gender = genderList[choice - 1]

    return gender


# Submenu for events, provides type check validation for the input and returns event type as a string
def event_picker():
    flag = True

    while flag:

        print("####################################################")
        print("################## Event Types #####################")
        print("####################################################")
        print("")
        print("########## Please select an issue type ##########")
        print("### 1. 100 Metres")
        print("### 2. 200 Metres")
        print("### 3. 400 Metres")
        print("### 4. 5 Kilometres")
        print("### 5. 10 Kilometres")
        print("### 6. Half Marathon")
        print("### 7. Marathon")

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

    eventList = ["100m", "200m", "400m", "5k", "10k", "Half Marathon", "Marathon"]

    event = eventList[choice - 1]

    return event


# Creates a new dataframe then counts the number of occurences of the requested issue type

def get_one_event_results(menu_choice):
    df = read_df()  # Improved this line by adding a

    eventresults = df[df['Event']== menu_choice]

    return eventresults


## New subroutine to generate the task 1 results of all results for 1 specific gender
def get_gender_results(menu_choice):
    df = read_df()
    genderresults = df[df['Gender'] == menu_choice]

    return genderresults


def main():

    chkflg = True

    while chkflg:

        main_menu_choice = main_menu()

        if main_menu_choice == "1":
            menu_choice = event_picker()
            print(get_one_event_results(menu_choice))
        elif main_menu_choice == "2":
            menu_choice = gender_picker()
            print(get_gender_results(menu_choice))



        elif main_menu_choice == "15":
            quit()

        else:
            print("Not a valid Menu option")


if __name__ == "__main__":
    main()