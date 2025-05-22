import pandas as pd  # Imports Pandas as PD Standard convention
import csv  # imports csv to work with the csv file
import matplotlib.pyplot as plt # imports pyplot to make graphs


def grapher(data,title):

    data.plot.bar()
    plt.title(title)
    plt.show()

def working():
    df = read_df()
    df = df[["Region"]]
    
    grapher(df, "Regions in the frame")

# Outputs the initial menu and validates the input
def main_menu():
    flag = True

    while flag:

        print("####################################################")
        print("############# Botes Parcels CRM System #############")
        print("####################################################")
        print("")
        print("########### Please select an option ################")
        print("### 1. Total issues by type")

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

  # Submenu for totals, provides type check validation for the input and returns issue type as a string
def total_menu():
    flag = True

    while flag:

        print("####################################################")
        print("############## Total issues by type ################")
        print("####################################################")
        print("")
        print("########## Please select an issue type ##########")
        print("### 1. Customer Account Issue")   
        print("### 2. Delivery Issue") 
        print("### 3. Collection Issue")  
        print("### 4. Service Complaint")

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

    issueTypeList = ["Customer Account Issue", "Delivery Issue", "Collection Issue", "Service Complaint"]
    

    issueType = issueTypeList[choice-1]
  
    return issueType     

# Creates a new dataframe then counts the number of occurences of the requested issue type

def get_total_data(total_menu_choice):
    
    issues = pd.read_csv("Task4a_data.csv")
    
    total = issues['Issue Type'].value_counts()[total_menu_choice]

    msg = "The total number of issues logged as a {} was: {}".format(total_menu_choice, total)
    return msg


def main():
    flag = True

    while flag:
        main_menu_choice = main_menu()
        if main_menu_choice ==  "1":
            total_menu_choice = total_menu()
            print(get_total_data(total_menu_choice))
        elif main_menu_choice == "2":
            pass
        elif main_menu_choice == "3":
            pass
        elif main_menu_choice == "4":
            quit


if __name__ == "__main__":
    main()

