from choose_seat import *
from seat_filter import *
import threading


possible_seats = possible_seats

def reserve_time(chosen_seat, t_):
    
    # print("For how long do you want to reserve the seat? Please enter hours, minutes and seconds.")
    # h = int(input("Enter hours."))
    # m = int(input("Enter minutes."))
    # s = int(input("Enter seconds."))
    # total_seconds = h * 3600 + m * 60 + s
    global seats
    global possible_seats

    while t_ > -1:
        timer = datetime.timedelta(seconds = t_)
        time.sleep(1)
        t_ -= 1
        
    seats.loc[seats.ID == chosen_seat, 'taken'] = 0
    students.loc[students.student_id == studentid, 'current_seat'] = 0
    
    possible_seats.append(chosen_seat)
    possible_seats.sort()

    return possible_seats



def final(chosen_seat, reserved_time):
    x = threading.Thread(target = reserve_time, args=([chosen_seat, reserved_time]))
    x.start()



