import pandas as pd
import csv
import matplotlib.pyplot as plt
from datetime import datetime

## CHECKER sections and key features

def read_df():
    df = pd.read_csv("Task4_sample_data.csv", parse_dates=["Date"], dayfirst=True)
    return df


# New subroutine to plot graphs and set title and y label.
def grapher(data, title, ylabel):
    data.plot()
    plt.title(title)
    plt.ylabel(ylabel)
    plt.show()


# new subroutine to check the validity of dates
def date_checker(date):
    ## important Import time and date at the top

    date_format = "%d/%m/%Y"  # key thing, Y is a caps not lowercase.

    try:
        # Try to parse the string with the expected format
        datetime.strptime(date, date_format)
        return True
    except ValueError:
        # If a ValueError is raised, the date is invalid (e.g., Feb 30th)
        return False


## Main menu

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
        print("### 3. All Results for one Date - Task 2")
        print("### 4. All Results for one Athlete - Task 3")
        print("### 5. All Results for a Date range - Task 4")
        print("### 6. All Earnings for one Athlete - Task 5")
        print("### 7. All Earnings for each Athlete - Task 6")

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


## PICKERS

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


# new subroutine to select an athlete for the results.
def athlete_picker():
    flag = True

    while flag:

        print("####################################################")
        print("################# Athlete Picker ###################")
        print("####################################################")
        print("")
        print("########## Please select an issue type ##########")
        print("### 1. Diego Silva")
        print("### 2. Aisha Khan")
        print("### 3. Mateo García")
        print("### 4. Fatima Al-Mansouri")
        print("### 5. Chen Wei")
        print("### 6. Kwame Mensah")
        print("### 7. Emily Connor")
        print("### 8. Sofia Rossi")
        print("### 9. Lars Johansson")
        print("### 10. Hiroshi Tanaka")

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

    athleteList = ["Diego Silva", "Aisha Khan", "Mateo García", "Fatima Al-Mansouri", "Chen Wei", "Kwame Mensah", "Emily Connor", "Sofia Rossi", "Lars Johansson", "Hiroshi Tanaka"]

    athlete = athleteList[choice - 1]

    return athlete



## Processors

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


# new subroutine for task 2 which gets events for a set date.
def get_date_results():
    df = read_df()
    chkflg = True

    while chkflg:
        wanted_date = input('Enter your date selection here (format dd/mm/yyyy): ')

        if date_checker(wanted_date):
            chkflg = False
        else:
            print("Sorry, you did not enter a valid date")

    df = df[df['Date'] == wanted_date]

    return df


#new subroutine to get results for one athlete only
def get_athlete_results(menu_choice):
    df = read_df()
    athleteresults = df[df['Athlete'] == menu_choice]

    return athleteresults


def get_date_range_results():
    df = read_df()
    chkflg = True

    while chkflg:
        start_date = input('Enter your start date selection here (format dd/mm/yyyy): ')
        end_date = input('Enter your end date selection here (format dd/mm/yyyy): ')

        if date_checker(start_date) and date_checker(end_date):
            chkflg = False
        else:
            print("Sorry, you did not enter a valid date")

    start_date = pd.to_datetime(start_date, format='%d/%m/%Y')
    end_date = pd.to_datetime(end_date, format='%d/%m/%Y')

    df = df[df['Date'].between(start_date, end_date)]

    return df

# new subroutine for task 5 to show earnings for one athlete.
def total_athlete_earning(menu_choice):
    df = read_df()
    df = df[df['Athlete'] == menu_choice]
    df = df[["Prize Money"]]

    return df["Prize Money"].sum()

# new subroutine for task 6 to show earnings per athlete
def athlete_earnings():
    df = read_df()
    df = df[['Athlete','Prize Money']]
    df = df.groupby("Athlete").sum()

    return df


# Added a main subroutine as needed under industry standard.
def main():

    chkflg = True  # establish a checkflag for the loop

    while chkflg:

        main_menu_choice = main_menu()

        if main_menu_choice == "1":
            menu_choice = event_picker()
            print(get_one_event_results(menu_choice))
        elif main_menu_choice == "2":
            menu_choice = gender_picker()
            print(get_gender_results(menu_choice))
        elif main_menu_choice == "3":
            print(get_date_results())
        elif main_menu_choice == "4":
            menu_choice = athlete_picker()
            print(get_athlete_results(menu_choice))
        elif main_menu_choice == "5":
            print(get_date_range_results())
        elif main_menu_choice == "6":
            menu_choice = athlete_picker()
            print(f"The total Earnings for {menu_choice} is £{total_athlete_earning(menu_choice)}")

        elif main_menu_choice == "7":
            earn = athlete_earnings()
            grapher(earn, "Earnings for each Athlete", "Value in £")
            print("The Earnings per Athelete")
            print(earn)

        else:  # added a final check for if no valid option choice found
            print("Not A valid menu choice")  # error message before looping again


# added new way to launch code, using industry standard convention
if __name__ == "__main__":
    main()