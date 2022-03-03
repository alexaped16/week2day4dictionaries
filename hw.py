#1) Create a program that allows a user to continue to add people to an address book until the user quits. 
# Once the user quits, break out of the loop and print out the name and address of everyone in the address book
#Steps


#Create a function that will ask user for name and addresses and stores them in a dictionary
#Define an empty dictionary with which to work (global or local variable?)
#Begin a loop that will continue to ask a user for information until the user "quits"
#If the user does not quit, ask for a name and address and store the variables into variables
#Add information to the dictionary with name as the key and address as the value
#If the user does quit, end the loop
#Print out the information from the dictionary in a formatted way
#Execute/Call the function


def address_book(start_program):

    #set flag to indicate that polling is active
    user_is_active = True
    user_info={}
    while user_is_active:

        #prompt user for their (name: address)
        k=input("Please enter person's name: ").lower() 
        v=input("Please enter person's address: ").lower() 

        #store (name:address) in dictionary
        user_info[k]= v
        question1 = input("Would you like to send this person a letter? ").lower()
        question2 = input("Would you like to send this person a gift? ")
        question3 = input("Would you like to add another name? Yes or No ").lower()
        if question3 == 'no': 
             user_is_active = False

        #user input is complete (print results)

        for k, v in user_info.items():
            print(f"{k}'s address is {v}")
        
(address_book(1))

#exercise 2) Best Time to Meet
#Billy is trying to figure out if there is a time that he and his team can meet to work on the project.
#His three teammates each give him a list of times they are available ('HH:MM' 24-hour). 
# Create a function that will take in the list of all the teammates and return a list of times where everyone can meet.


billy_times = ['09:00', '10:30', '11:30', '12:00', '13:00', '14:30']
teammate_1 = ['09:30', '10:00', '10:30', '12:00', '14:30', '16:00']
teammate_2 = ['09:00', '09:30', '11:00', '11:30', '12:00', '13:30', '14:30', '15:00']
teammate_3 = ['11:00', '11:30', '12:00', '14:00', '14:30', '16:30', '17:00']
# Available Times: '12:00' and '14:30'


def available(set_a,set_b,set_c, set_d):
    billy_set = set(set_a)
    teammate_1_set = set(set_b)
    teammate_2_set = set(set_c)
    teammate_3_set = set(set_d)
    available_times = billy_set & teammate_1_set & teammate_2_set & teammate_3_set
    return(available_times)
print(available(billy_times, teammate_1,teammate_2,teammate_3))







        

