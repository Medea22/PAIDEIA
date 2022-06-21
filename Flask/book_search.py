import pandas as pd
import numpy as np

books = pd.read_pickle("/Users/medea/Documents/Ironhack/PAIDEIA_library/Library/Data/books_with_section.p")
students = pd.read_pickle("/Users/medea/Documents/Ironhack/PAIDEIA_library/Library/Data/students.p")

filtered_books = pd.DataFrame(columns= books.columns)

# def search():
#     global studentid
#     global filtered_books

#     filtered_books = pd.DataFrame(columns= books.columns)

#     studentid = int(input("Please enter your student ID."))
#     password = int(input("Please enter your passwords."))

#     if password == students.loc[students["student_id"] == studentid, "password"][0]:
#         filters()
#     else: 
#         print("Student ID or password incorrect. Please try again.")
#         search()

def filters():

    global filtered_books
    
    print("Please choose a filter.")
    print("You can choose between genre, year, title, and author or type 'stop' for end filtering.")

    f = input("Please enter the filter of your choice.").lower()

    if f == "genre":
        genre()
        filters()
    elif f == "year":
        year()
        filters()
    elif f ==  "title":
        title()
        filters()
    elif f == "author":
        author()
        filters()
    elif f == "stop":
        stop()
    else:
        print("Invalid entry.")
        filters()


def genre(g): 
        """
        Filter for specific genre.
        """
        global filtered_books

        #print("We have 8 genres:")
        #print("""For Arts & Music enter Z, for Business, Economics & Industry enter X, 
        #     Engineering & Programming enter T, for Kids & Fiction enter Y,
        #     for Law & Crime enter U, for Medicine enter V,
        #     for Social Science and Teaching enter W and for Other enter S.""")

        # genre = input("Please enter the letter of the genre of your choice.").upper()
        g =g.upper()

        if g in ["S", "T", "U", "V", "W", "X", "Y", "Z"]:
            x = books[books["section"] == g]
            filtered_books = pd.concat([filtered_books, x])   
        # else:
        #     print("Invalid entry.")
        #     genre(g)
                
    
def year(y):
    """
    Filter for specific publication year.
    """
    global filtered_books

    #books["year"] = pd.DatetimeIndex(books["publication-date"]).year

    #year = int(input("Please enter the year of publication."))
    #y = int(y)
    if y in list(books["year"].unique()):
        x = books[books["year"] == y]
        filtered_books = pd.concat([filtered_books, x])
    
    # else:
    #     print("Invalid entry.")
    #     year(y)

def title(t):
    """
    Ask for book title and give back best match and location.
    """
    global filtered_books

    #title = input("Please enter a book title or choose for a word.").lower()

    t = t.lower()
    books['title'] = books['title'].str.lower()
    x = books.loc[books['title'].str.contains(t)]
    filtered_books = pd.concat([filtered_books, x])
    

def author(a):
    """
    Filter for author name.
    """
    global filtered_books

    #auth = input("Please enter the author's last name.").lower()
    a = a.lower()
    books['authors'] = books['authors'].str.lower()
    x = books.loc[books['authors'].str.contains(a)]
    filtered_books = pd.concat([filtered_books, x])
    
    
def stop():
    """
    Stop filtering and display best matching books.
    """
    global ids
    global filtered_books

    ids = list(filtered_books["id"].mode())
    column_names = ["title", "authors", "year", "Genre", "section", "shelf", "id", "description", "format"]
    ordered = books[column_names]
    
    final = pd.DataFrame(columns = column_names)
    for i in ids:
        xx = ordered.loc[ordered["id"]==i]
        final = pd.concat([final, xx])
    filtered_books = pd.DataFrame(columns= books.columns)
    final["year"] = final["year"].astype("int")
    final["shelf"] = final["shelf"].astype("int")
    #return filtered_books
    return final.head()

    #found_book()
    
