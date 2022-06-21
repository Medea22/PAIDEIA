# libraries
import pandas as pd
import numpy as np
from collections import Counter
import time
import datetime

# datasets
seats = pd.read_csv("/Users/medea/Documents/Ironhack/PAIDEIA_library/Library/Data/seats.csv").drop(columns="Unnamed: 0")
students = pd.read_pickle("/Users/medea/Documents/Ironhack/PAIDEIA_library/Library/Data/students.p")

# empty list for seat selection
possible_seats = []
studentid = None

# functions
def reserve_seat():
    """
    Function that asks for login data and continues to functions that filter for seats.
    """
    global studentid
    global seats
    global possible_seats


    studentid = int(input("Please enter your student ID."))
    password = int(input("Please enter your passwords."))
 
    if password == int(students.loc[students["student_id"] == studentid, "password"]):
        print("There are", len(seats[seats["taken"]==0]), "seats available.")
        filtering()

        return possible_seats
        
    else: 
        print("Student ID or password incorrect. Please try again.")
        reserve_seat()

def filtering():
    """
    Function to decide wether or not to filter the availabe seats.
    """
    global studentid
    global seats
    global possible_seats

    filt = input("Do you want to filter the available seats?").lower()
    
    if filt == "yes":
        choose_filter()

    elif filt == "no":
        
        if len(possible_seats) == 0:

            seat = seats.loc[seats['taken'] == 0, 'ID']

            for i in seat:
                possible_seats.append(i)

            #return possible_seats


        

    
        
    else:
        print("Invalid entry. Please enter yes or no")
        filtering()

    #return studentid



def choose_filter():
    """
    Function to choose filter.
    """
    
    filt = input("Choose a filter: section, floor, windows, computer, toilet, elevator and stairs.").lower()
    if filt == "section":
        section()
    elif filt == "floor":
        floor()
    elif filt == "windows":
        window()
    elif filt == "computer":
        computer()
    elif filt == "toilet":
        toilet()
    elif filt == "elevator":
        elevator()
    elif filt == "stairs":
        stairs()
   

def section(sec):
    """
    Function to filter seats regarding their section in the library.
    """
    global seats
    global possible_seats
    print('inside function', possible_seats)


    lis_s = ["A", "B", "C", "D", "E", "F", "G", "H"]
    sec = sec.upper()
    if sec in lis_s:
        df = seats[seats["Area"]==sec]
        seat = df.loc[df['taken'] == 0, 'ID']

        for i in seat:
            possible_seats.append(i)

        #another = input("Do you want to choose another section?").lower()
        
        # if another == "yes":
        #     section()
            
    # else:
    #     print("Invalid entry. We don not have seats in this area.")
    #     section()
    

def floor(f):
    global seats
    global possible_seats
    f = f  #input("Which floor do you prefer: ground floor or first floor?").lower()

    if f == 0:
        df = seats[seats["z"]==0]
        seat = df.loc[df['taken'] == 0, 'ID']
        for i in seat:
            possible_seats.append(i)

    elif f == 1:
        df = seats[seats["z"]==1]
        seat = df.loc[df['taken'] == 0, 'ID']
        for i in seat:
            possible_seats.append(i)
    
    # else:
    #     print("Invalid entry.")
    #     floor()
        

def window(w):
    """
    Function to filter wether or not a place should be located close to the window.
    """
    global seats
    global possible_seats

    w = w.lower().strip() #input("Do you want to sit close to a window?").lower().strip()
    
    if w == "yes":
        df = seats[seats["Window"]==1]
        seat = df.loc[df['taken'] == 0, 'ID']
        for i in seat:
            possible_seats.append(i)
    
    elif w == "no":
        df = seats[seats["Window"]==0]
        seat = df.loc[df['taken'] == 0, 'ID']
        for i in seat:
            possible_seats.append(i)
    
    # else:
    #     print("Invalid entry. Please type yes or no.")
    #     window()

def computer(c):
    """
    Function to filter wether or not a computer is wanted.
    """
    global seats
    global possible_seats
    c = c.lower().strip()  # input("Do you want a place with a computer?").lower().strip()
    
    if c == "yes":
        df = seats[seats["Computer"]==1]
        seat = df.loc[df['taken'] == 0, 'ID']
        for i in seat:
            possible_seats.append(i)
    
    elif c == "no":
        df = seats[seats["Computer"]==0]
        seat = df.loc[df['taken'] == 0, 'ID']
        for i in seat:
            possible_seats.append(i)
    
    # else:
    #     print("Invalid entry. Please type yes or no.")
    #     computer()


def toilet(t):
    """
    Function to filter wether or not the seat should be close tot the toilets.
    """
    global seats
    global possible_seats
    t = t.lower().strip() #input("Do you want to sit close to or far from the toilet? Type close or far").lower().strip()
    
    if t == "close":
        df = seats[seats["dist_toilet"]<=5]
        seat = df.loc[df['taken'] == 0, 'ID']
        for i in seat:
            possible_seats.append(i)
    
    elif t == "far":
        df = seats[seats["dist_toilet"]>=6]
        seat = df.loc[df['taken'] == 0, 'ID']
        for i in seat:
            possible_seats.append(i)
    
    # else:
    #     print("Invalid entry.")
    #     toilet()


def elevator(e):
    """
    Function to filter wether or not the seat should be close tot the elevator.
    """
    global seats
    global possible_seats
    e = e.lower().strip() #input("Do you want to sit close to or far from the elevator? Type close or far").lower().strip()
    
    if e == "close":
        df = seats[seats["dist_elevator"]<=5]
        seat = df.loc[df['taken'] == 0, 'ID']
        for i in seat:
            possible_seats.append(i)
    
    elif e == "far":
        df = seats[seats["dist_elevator"]>=6]
        seat = df.loc[df['taken'] == 0, 'ID']
        for i in seat:
            possible_seats.append(i)
    
    # else:
    #     print("Invalid entry.")
    #     elevator()

def stairs(st):
    """
    Function to filter wether or not the seat should be close tot the stairs.
    """
    global seats
    global possible_seats
    st = st.lower().strip() #input("Do you want to sit close to or far from the stairs? Type close or far").lower().strip()
    
    if st == "close":
        df = seats[seats["dist_stairs"]<=5]
        seat = df.loc[df['taken'] == 0, 'ID']
        for i in seat:
            possible_seats.append(i)
    
    elif st == "far":
        df = seats[seats["dist_stairs"]>=6]
        seat = df.loc[df['taken'] == 0, 'ID']
        for i in seat:
            possible_seats.append(i)
    
    # else:
    #     print("Invalid entry.")
    #     stairs()
