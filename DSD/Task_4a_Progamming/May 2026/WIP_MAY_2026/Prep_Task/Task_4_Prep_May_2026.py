import pandas as pd
import csv
import matplotlib.pyplot as plt


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


# Submenu for events, provides type check validation for the input and returns event type as a string
def event_menu():
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
    df = pd.read_csv("Task4_sample_data.csv")

    eventresults = df[df['Event']== menu_choice]

    return eventresults


main_menu_choice = main_menu()
if main_menu_choice == "1":
    menu_choice = event_menu()
    print(get_one_event_results(menu_choice))

