# import imp
from mmap import PROT_WRITE
from multiprocessing import pool
from typing import final
from unittest import result
from flask import Flask, render_template, request, redirect, url_for
from book_search import *
from seat_filter import *
from choose_seat import *
from reserve_for_time import *
from preparing_text import *
from similarbooks import *

app = Flask(__name__)

class StoreSeat():
    choice = None

chair = StoreSeat()

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/books", methods=["POST","GET"])
def books():
    if request.method == "POST":
        g = request.form["genre"]
        t = request.form["title"]
        a = request.form["author"]
        if request.form["year"] != "":
            y = int(request.form["year"])
        else:
            y = 5

        if g != "":
            genre(g)
        if t != "":
            title(t)
        if a != "":
            author(a)
        if y != "":
            year(y)

        table_df = stop()#["description"].iloc[0]
        table_json = table_df.to_html(index=False)
    

        return render_template("books.html", table=table_json)
        
    return render_template("books.html")

@app.route("/seats", methods=["POST","GET"])
def find_seats():
    if request.method == "POST":
        sec = request.form["section"]
        if request.form["floor"] != "":
            f = int(request.form["floor"])
        else:
            f = 5
        w = request.form["window"]
        c = request.form["computer"]
        t = request.form["toilet"]
        e = request.form["elevator"]
        st= request.form["stairs"]

        seats['taken'] = np.where(((seats['taken'] == 1) | (seats['taken'] == 'taken')), 1, 0)

        if sec != "":
            section(sec)
        if f != "":
            #print(type(f))
            floor(f)
        if w != "":
            window(w)
        if c != "":
            computer(c)
        if t != "":
            toilet(t)
        if e != "":
            elevator(e)
        if st != "":
            stairs(st)
        
        print('outside', possible_seats)
        val = best_seats(possible_seats)

        chair.choice = val

    
        return redirect("/reserve_seat")
    return render_template("seats.html")


@app.route("/reserve_seat", methods=["POST","GET"])
def book_seat():
    global seats
    if request.method == 'POST':

        hour = int(request.form['hour'])
        minute = int(request.form['minute'])
        second = int(request.form['second'])

        seat_number = int(request.form['seatno'])

        total_seconds = hour * 3600 + minute * 60 + second

        seats.loc[seats.ID == seat_number, 'taken'] = 1
        seats['taken'] = np.where(((seats['taken'] == 1) | (seats['taken'] == 'taken')), 'taken', 'empty')

        final(seat_number, total_seconds)
        print(seats.loc[seats["ID"] == seat_number, "taken"])
        return render_template('booktry.html', seats=seats)
        
    else:

        seats['taken'] = np.where(((seats['taken'] == 1) | (seats['taken'] == 'taken')), 'taken', 'empty')
        return render_template('booktry.html', seats=seats, chair= chair.choice)


@app.route("/suggestions", methods=["POST","GET"])
def suggestions():

    if request.method == 'POST':

        genre = request.form['genretype'].strip()
        text = request.form['summary']

        table_df = get_cluser(genere=genre, text=text)

        table_json = table_df.to_html(index=False)

        return render_template("suggestions.html", table= table_json)


    return render_template("suggestions.html")


@app.route("/user" , methods=["POST","GET"])
def user():
    if request.method == "POST":
        studid = int(request.form['student_id'])
        password = int(request.form['password'])
    
        condition = ((studid == 123456) & (password == 1234560))

        if condition == True:
            login =  True
            return render_template("user.html", login = login)
        
        elif condition == False:
            failed = True
            return render_template("user.html", failed = failed)
    return render_template("user.html")





if __name__ == "__main__":
    app.run(debug=True)