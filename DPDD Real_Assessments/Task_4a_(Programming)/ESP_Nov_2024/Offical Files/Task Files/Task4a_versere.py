import pandas as pd

def main_menu():
    flag = True

    while flag:

        print("#################################################")
        print("############## Versere Cars Sales ##############")
        print("#################################################")
        print("")
        print("########### Please select an option #############")
        print("### 1. Total Sales Analysis")

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

def total_menu ():
    flag = True

    while flag:

        print("#################################################")
        print("############## Total Sales ##############")
        print("#################################################")
        print("")
        print("########### Please select an option #############")
        print("### 1. All sales by model")   
        print("### 2. Custom selection") 

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

def convert_total_menu_coice(total_menu_choice):
    
    if total_menu_choice == "1":
        total_choice = "All"
    else:
        total_choice = "Model"  
    
    return total_choice

def get_total_data(total_choice):
    
    df = pd.read_csv("Task4a_data.csv")

    if total_choice == "All":
        extract = df.groupby(['Date','Car Model'], sort=True)['Value'].sum()
        total = df['Value'].sum()
        print("The total value of sales for your selection is {}".format(total))

    else:
        flag = True

        while flag:

            print("########### Please select a model #############")
            print("### 1. Ranger")
            print("### 2. Model D Premium Plus")
            print("### 3. Compass")
            print("### 4. Mercury")
            print("### 5. Outback")
            
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

        models = ["Ranger", "Model D Premium Plus", "Compass", "Mercury", "Outback"]   

        custom_choice = models[choice -1]

        extract = df.loc[df['Car Model'] == custom_choice]
        total = extract['Value'].sum()
        print("The total value of sales for your selection is {}".format(total))

    

    return extract

main_menu_choice = main_menu()

if main_menu_choice == "1":
    total_menu_choice = total_menu()
    total_choice = convert_total_menu_coice(total_menu_choice)
    print(get_total_data(total_choice))
else:
    print("This section is under construction")
