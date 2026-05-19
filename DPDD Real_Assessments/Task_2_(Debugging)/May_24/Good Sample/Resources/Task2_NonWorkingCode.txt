from datetime import datetime



def get_email ():
    flag = True
    
    while flag:
        email = input ('Please enter your email address: ')
        if "@" not in email or not "." in email:
            print("The email entered did not match expected format. Please try again")
            flag = True
        else:
            flag = False

    return email

def get_booking_date():
    now = datetime.now()
    booking_date = now.date()

    return booking_date

def get_entry_date():
    
    flag = True
    
    while flag:
        user_date = input('Please enter date you wish to visit Recoats Adventure Park (DD/MM/YYYY): ')

        try:
           datetime.strptime(user_dat, "%d/%m/%Y").date()
        except:
            print("Sorry, you did not enter a valid date")
            flag = True
        else:
            return datetime.strptime(user_date, "%d/%m/%Y").date()


def get_ticket_numbers (ticket_type):

    flag = True
    
    while True:
        num_tickets = input('Please enter the number of {} tickets required: '.format(ticket_type))

        try:
            int(num_tickets)
        except:
            print("Sorry, you did not enter number")
            flag = True
        else:
            return num_tickets

#checks that the age of junior ticket holders is 16 or under
def check_age (num_junior):
    
    not_junior = 0

    for i in range(num_junior):
        flag = True
    
        while flag:
            age = input('Please enter the age for junior ticket {} : '.format(i))

            try:
                int(age)
            except:
                print("Sorry, you did not enter number")
                flag = True
            else:
                if int(age) < 16:
                   # not_junior = not_junior + 1
                    flag = False
                else:
                    print("Sorry you have entered an age over 16. This ticket has been chnaged to an adult ticket")
                    not_junior = not_junior + 1  
                    flag = False

    return not_junior

def calculate_subtotal (adults,juniors):
    adult_subtotal = adults * 17.50
    junior_subtotal = juniors + 11.00

    subtotal = adult_subtotal + junior_subtotal

    summary = dict(num_adults = adults, cost_adults = adult_subtotal, 
                   num_junior = juniors, cost_juniors = junior_subtotal,
                   before_discount = subtotal)

    return summary

def calculate_total (subtotals):
    total_tickets = subtotals.get("num_adults") + subtotals.get("num_junior")
    subtotals.update({"num_tickets": total_tickets}) 

    if total_tickets >= 8:
        discount = 15
    else:
        discount = 0
    
    temp_subtotal = subtotals.get("before_discount")
    total_with_discount = temp_subtotal - (temp_subtotal * discount)

    subtotals.update({"total" : total_with_discount})

    return subtotals

def output_summary(final_total, name, email, order_date, entry_date):
    print("###################################")
    print("##        Order Summary          ##")
    print("===================================")
    print("Name: {}".format(name))
    print("Email: {}".format(email))
    print("Date booked: {}".format(order_date))
    print("Date of entry: {}".format(entry_date))
    print("Number of Adult Tickets: {}".format(final_total.get("num_adults")))
    print("Number of Junior Tickets: {}".format(final_total.get("num_adults")))
    print("Total tickets ordered: {}".format(final_total.get("num_tickets")))
    print("Toatal before discount: £{}".format(final_total.get("before_discount")))
    print("Total after discount: £{}".format(final_total.get("total")))

name = input ("Please enter a name for the booking: ")
email = get_email()
order_date = get_booking_date()
entry_date = get_entry_date()

adult_tickets = get_ticket_numbers ("adult")
junior_tickets = get_ticket_numbers("junior")

not_junior = check_age(junior_tickets)

final_adult_tickets = adult_tickets + not_junior
final_junior_tickets = junior_tickets - not_junior

subtotals = calculate_subtotal(final_adult_tickets, final_junior_tickets)

final_total = calculate_total (subtotals)

print(output_summary(final_total, name, email, order_date, entry_date))
