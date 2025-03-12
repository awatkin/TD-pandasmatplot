import pandas as pd
import matplotlib.pyplot as plt  # added import statement to allow graphing to be done

def dfreadin():  #added a subroutine so DF is only created in one place for maintainability and readability
    df = pd.read_csv("Task4a_data.csv")
    return df

def makegraph(df,graph_type, title, x_axis, y_axis):  # new subroutine to call to make a graph
    if graph_type == "bar":  # checks if it should be a bar chart
        df.plot.bar()  # plots as a bar chart if true
    else:
        df.plot()  # if not, builds a normal graph
    plt.title(title)  # Sets the title of the plot based on user input
    plt.xlabel(x_axis)  # sets the x axis from the parameter
    plt.ylabel(y_axis)  # Sets the y axis label based on the user set parammeter
    plt.show()  # shows the graph

def post_type_select():
    flag = True

    while flag:

        print("#################################################")
        print("############ Time of Day Interaction ############")
        print("#################################################")
        print("")
        print("########### Please select an option #############")
        print("### 1. Likes Performmance")
        print("### 2. Shares Performance")
        print("### 3. Comments Performance")
        print("### 4. All interactions Performance")

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

def main_menu():
    flag = True

    while flag:

        print("#################################################")
        print("############## Snowy Animal Rescue ##############")
        print("#################################################")
        print("")
        print("########### Please select an option #############")
        print("### 1. Average Social Media Interaction Data")
        print("### 2. Popularity of each post type")  # added new option to allow looking at popularity of each type of post
        print("### 3. Time of day performance for posts")  # Added a new option to search for performance at times of day
        print("")
        print("### 7. Quit")

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


def average_menu ():
    flag = True

    while flag:

        print("#################################################")
        print("############## Average Interaction ##############")
        print("#################################################")
        print("")
        print("########### Please select an option #############")
        print("### 1. Average number of Likes")   
        print("### 2. Average number of Shares") 
        print("### 3. Average number of Comments")  

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

def convert_avg_men_coice(avg_men_choice):
    
    if avg_men_choice == "1":
        avg_choice = "Likes"
    elif avg_men_choice == "2":
        avg_choice = "Shares"
    else:
        avg_choice = "Comments"  
    
    return avg_choice


def get_avg_data(avg_choice):
    
    df = dfreadin()  # altered the code to read in from the new DFreadin subroutine to make it clearly and more maintainable
    extract = df.groupby(['Date'], as_index=False) [avg_choice].mean()
    extract_no_index = extract.to_string(index=False)
    
    print("Here is the average number of {} each day during the campaign:".format(avg_choice))
    return extract_no_index


def post_popularity():  # new subroutine to total the interactions for each post type
    df = dfreadin()  # Bringss in the dataframe
    extract = df[["Post Type","Likes","Shares","Comments"]]  # slices the data frame to the columns needed
    extract = extract.groupby("Post Type").sum()  # first stge to group by post type and sum the types of interationc

    highest_likes = extract['Likes'].idxmax()
    highest_comments = extract['Comments'].idxmax()
    highest_shares = extract['Shares'].idxmax()

    print("Here are the totals for each interaction type for each type of post")  # Friendly way to output the information
    print("")
    print(extract)  # initial results of totaling
    print("")
    #extract =  extract.sum(axis=1)
    extract['Total Interactions'] = extract.sum(axis=1)  # Totals interations of any type for each post type
    highest_inter = extract['Total Interactions'].idxmax()
    print("")
    print("The Post type with the highest likes is: ", highest_likes)
    print("")
    print("The Post type with the highest Comments is: ", highest_comments)
    print("")
    print("The Post type with the highest shares is: ", highest_shares)
    print("")
    print("The post type with the highest interactions over all is: ", highest_inter)
    print("")
    print("Here is the total interactions for each post type")  # friendly way to output
    print(extract)  # prints out the results
    return extract,"bar", "Total Interactions per type","Interaction type", "Total Interations"


def time_of_day_performance(type_to_use):  # new sub routine to look at performance through the day
    graph_type = ""  # sets variable to collect graphs type
    title = ""  # sets variable to collect graph title
    x_axis = ""  # variable to collect X axis label
    y_axis = ""  # variable to collect the y axis label
    df = dfreadin()  # collects a fresh dataframee to maniputlate


def main():
    while True:
        main_menu_choice = main_menu()
        if main_menu_choice == "1":
            avg_men_choice = average_menu()
            avg_choice = convert_avg_men_coice(avg_men_choice)
            print(get_avg_data(avg_choice))
        elif main_menu_choice == "2":  # added a new menu option for the popularity of each typee of post
            df, graph_type, title, x_axis, y_axis = post_popularity()
            makegraph(df, graph_type, title, x_axis, y_axis)
        elif main_menu_choice == "3":
            type_to_use = post_type_select()
            df, graph_type, title, x_axis, y_axis = time_of_day_performance(type_to_use)
            makegraph(df, graph_type, title, x_axis, y_axis)
        elif main_menu_choice == "7":
            print("Thanks for using our system, Goodbye")
            quit()


if __name__ == "__main__":  #added a suitable starting to code for coding conventions
    main()  # calls main when