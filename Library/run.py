from reserve_for_time import *



if __name__ == "__main__":
    
    i = 0
    while i < 10:
        i +=1
        seat = reserve_seat() 
        chosen_seat = best_seats(seat)
        print(chosen_seat)
        print("For how long do you want to reserve the seat? Please enter hours, minutes and seconds.")
        h = int(input("Enter hours."))
        m = int(input("Enter minutes."))
        s = int(input("Enter seconds."))
        total_seconds = h * 3600 + m * 60 + s
        
        final(chosen_seat, total_seconds)