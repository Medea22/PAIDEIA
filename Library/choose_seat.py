from seat_filter import *

chosen_seat = None
possible_seats = possible_seats


def best_seats(p_seats):
    """
    Function that presents the best seats and lets you choose one that will be reserved.
    """
    global chosen_seat
    global seats
    global studentid
    global possible_seats #

    possible_seats = p_seats # 

    seat_freq = dict(Counter(p_seats))
    seat_dict = seat_freq
    max_value = max(seat_freq.values())
    choice = [k for k,v in seat_dict.items() if v == max_value]

    print("Following seats are optimal for you:", choice)

    chosen_seat = int(input("Please enter the ID of the place you want to reserve."))

    if chosen_seat in choice:

        seats.loc[seats.ID == chosen_seat, 'taken'] = 1
        students.loc[students.student_id == studentid, 'current_seat'] = chosen_seat
        print("Your seat with the ID" , chosen_seat , "has been reserved.")
        
        #print(possible_seats) #
        possible_seats.remove(chosen_seat)
        return chosen_seat
        
    else:
        print("This seat is not available. Make sure that you enter the correct ID.")
        best_seats()
    
    
