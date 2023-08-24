
# --------------------- PROJECT : RAILWAY TICKET BOOKING -----------------------

""" Description:
   This program is for booking railway ticket.

   It includes classes: Account, Traininfo, Passenger, Ticket

   1. Account class is defined with constructor that takes two arguments username and password
      It has method to check the password that matches the stored password.

   2. Traininfo class represents a train with its train number, source, destination, 
      and the number of seats available. 
      It has methods to display the train information and book tickets.

   3. Passenger class represents a passenger with their name, age, gender, and phone number. 
      It has a method to display passenger information.

   4. Ticket class represents a ticket with the train, source, destination, passengers, and 
      PNR (Passenger Name Record) number. 
      It has a method to display ticket information.

"""
# source code with comments

#  We start by importing the random module, which we'll 
#  use to generate random PNRs for the tickets later on

import random

# Account class is defined with a constructor that takes two arguments:username and password. 
# This class defines a method called check_password which takes a single argument password and returns 
# a boolean indicating whether the input password matches the stored password.

class Account :
    def __init__(self,username,password):
        self.username =username
        self.password =password
    def checkpassword(self,password):
         return self.password == password
    
#  We define the Train class, which takes in four parameter train_num, source, destination, avl_seats 
#  The __init__() method is called when a new Train object is created and initializes these attributes.

class Traininfo:

    def __init__(self,train_num,source,destination,avl_seats):
        self.train_num = train_num
        self.source = source
        self.destination = destination
        self.avl_seats = avl_seats

#  We define a display_info() method for the Train class, 
#  which displays train_num, source, destination, avl_seats for a given train object.

    def displayinfo(self):
        print(f"Train number:{self.train_num}")
        print(f"Source: {self.source}")
        print(f"Train Destination:{self.destination}")
        print(f"Availabile seats: {self.avl_seats}")

#  We define a book_tickets() method for the Train class, 
#  This method takes a number of tickets as input and attempts to book that many tickets on the train. 
#  If there are enough available seats, the method generates a list of random PNRs equal to the number 
# of tickets being booked, updates the number of available seats, and returns the list of PNRs.
# Otherwise, the method returns None to indicate that the booking failed.
# The book_tickets method takes in the number of tickets to be booked and returns a list of PNR numbers 
# for the tickets if they are available, or None if there are not enough seats.

    def book_tickets(self, num_tickets):
        if num_tickets > self.avl_seats:
            return None
        else:
            pnr_list = []
            for i in range(num_tickets):
                pnr_list.append(random.randint(100000, 999999))
            self.avl_seats -= num_tickets
            return pnr_list


# The Passenger class is defined, which takes in four parameters - name, age, gender, and phone_num. 
# These parameters are used to initialize the attributes of the Passenger object.

class Passenger:
    def __init__(self, name, age, gender, phone_num):
        self.name = name
        self.age = age
        self.gender = gender
        self.phone_num = phone_num

#  Passenger class has display_info method,which prints name,age,gender,and phone_num of the passenger.
     
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Phone Number: {self.phone_num}")

# Ticket class is defined, which takes in five parameters: train, source, destination, passengers, and pnr. 
# These parameters are used to initialize the attributes of the Ticket object.

class Ticket:
    def __init__(self, train, source, destination, passengers, pnr):
        self.train = train
        self.source = source
        self.destination = destination
        self.passengers = passengers
        self.pnr = pnr

# Ticket class has a method called display_info, which prints out 
# the train number, source, destination, PNR number, and the information of each passenger.

    def display_info(self):
        print(f"Train Number: {self.train.train_num}")
        print(f"Source: {self.source}")
        print(f"Destination: {self.destination}")
        print(f"PNR: {self.pnr}")
        for passenger in self.passengers:
            passenger.display_info()
        print()

# A list called accounts is initialized with two Account objects already in it, 
# with the usernames "user1" and "user2" and passwords "password1" and "password2" respectively.

accounts = [
    Account("user1","password1"),
    Account("user2", "password2")
]

# A variable called logged_in_account is initialized to None. 
# This variable will be used later to keep track of the currently logged-in account.

logined_account = None

# A while loop is started that will run indefinitely until the user logs in successfully 
# It is presented with the available train details.

# Inside the loop, the user is presented with two options: either to create an account or to login. 
# The user's option is stored in a variable called choice.

while True:
    print("Select the options")
    print("1.To create an acount:\n2.To login account")
    option = int(input("enter your option: "))
# If the user chooses to create an account (option == "1"), they are prompted 
# to enter a username and password. 
# The inputted username and password are then used to create a new Account object,
# which is appended to the accounts list.
    if option == 1:
        username= input("Enter username: ")
        password =input("Enter password: ")
        accounts.append(Account(username,password))
        print("account created succesfully")
# If the user chooses to login (option == "2"), they are prompted to enter a username and password. 
# The program then iterates through the accounts list and checks if any of the stored accounts match 
# the inputted username and password. 
# If a match is found, the corresponding Account object is assigned to the logged_in_account variable 
# and the loop is broken. Otherwise, an error message is printed.

    elif option ==2:
        username = input("Enter username: ")
        password = input("Enter password: ")
        for account in accounts:
            if account.username == username and account.checkpassword(password):
                 logined_account = account
                 break
        if logined_account is None:
            print("invalid username or pasword")
        else:
            print(
                f"\nLogged in as {logined_account.username}\n\n-----Availabe Train details-----\n")

            break
    else:
        print("Invalid choice.")
       
# The program creates a list of Train objects, with each train having a unique 
#  train_num, source, destination, avl_seats

if logined_account is not None:
    trains =[
        Traininfo("12603","Chennai","Hyderabad",120),
        Traininfo("17023","Shadnagar","Secundrabad",212),
        Traininfo("17569","Secundrabad","Tirupathi",189)
    ]

# If the logged_in_account variable is not None, it means that the user has successfully logged in. 
# A message is printed confirming the login, and then a list of available train details is printed.
for train in trains:
    train.displayinfo()


# Get user input for booking
# If the number of tickets entered is more than the available seats, 
# it will raise a ValueError with the message "Selected more tickets than available seats".
# The program asks the user to enter the train number and the number of tickets they want to book.

while True:
    try:
        train_num = input("Enter Train Number: ")
        num_tickets = int(input("Enter Number of Tickets: "))
        if num_tickets <= 0:
            raise ValueError("Number of tickets should be greater than 0")
        for train in trains:
            if train.train_num == train_num:
                if num_tickets > train.avl_seats:
                    raise ValueError(
                        "Selected more tickets than available seats") 
                break
        else:
            raise ValueError("Invalid Train Number.")
        break
    except ValueError as e:
        print(f"Invalid Input: {e}")

# The program then searches for the Train object with the corresponding train number entered by the user.

train = None
for t in trains:
    if t.train_num == train_num:
        train = t
        break

# If the train number is invalid, the program prints "Invalid Train Number." and exits.

if train is None:
    print("Invalid Train Number.")

# If the train number is valid, the program prompts the user to enter the details of each passenger.
# For each passenger, the program creates a Passenger object with the name, age, gender, and phone number entered by the user and appends it to a list of passengers.

else:
    passengers = []
    for i in range(num_tickets):
        print(f"\nEnter details for Passenger {i + 1}:")
        while True:
            try:
                name = input("Name: ")
                if not name:
                    raise ValueError("Name cannot be empty")
                age = int(input("Age: "))
                if age <= 0 or age > 120:
                    raise ValueError("Invalid Age")
                gender = input("Gender: ")
                phone = input("Phone Number: ")
                if not phone or len(phone) != 10 or not phone.isdigit():
                    raise ValueError("Invalid Phone Number")
                passenger = Passenger(name, age, gender, phone)
                passengers.append(passenger)
                break
            except ValueError as e:
                print(f"Invalid Input: {e}")

# The program calls the book_tickets method of the Train object to book the tickets. 
# If there are enough seats available, the book_tickets method returns a list of PNR numbers for 
# the tickets, which the program saves in a list called pnr_list.
# If there are not enough seats available, the book_tickets method returns None, and the program 
# prints "Tickets not available." and exits.

    pnr_list = train.book_tickets(num_tickets)
    if pnr_list is None:
        print("Tickets not available.")

# Program prints "Booking Successful!", If tickets are successfully booked.
# Creates Ticket object for each passenger with the train, source, destination, passenger info,and PNR no. 
# Program calls display_info method of each Ticket object to display the information to the user.

    else:
        print("\n--------------Booking Successful!------------\n\nYour Ticket Details: \n")

        for i in range(num_tickets):
            ticket = Ticket(train, train.source, train.destination, [
                            passengers[i]], pnr_list[i])
            ticket.display_info()
            print("\n--------Thank You------- \n-------Safe Journey------")




# -------- FINISHED--------






