import sqlite3

def getconnection():
    try:
        con = sqlite3.connect("C:\sqlite\moviemanager.db")
        if(con):
            print("You are connected with database")
            return con
    except sqlite3.Error as e:
        print("There is problem connecting with database: ", e)

def addmovies(data):
    try:
        con = getconnection()
        cur = con.cursor()
        sql = "Insert into movies(title, genre, rating) values (?,?,?);"
        if(cur.execute(sql,data)):
            print("Your movies has been updated in database!!")
        cur.close()
        con.commit()
    except sqlite3.Error as e:
        print("There is problem in updating the movies in database: ",e)
    finally:
        if(con):
            con.close()

def searchmovies(genre):
    try:
        con = getconnection()
        cur = con.cursor()
        sql = "select * from movies where genre = ?;"
        cur.execute(sql,(genre,))
        rows = cur.fetchall()
        for data in rows:
            print("Genre: ",data[2], "  Title: ",data[1], "  Rating: ",data[3])
        cur.close()
        return True
    except sqlite3.Error as e:
        print("There is problem in searching movies: ",e)
    finally:
        if(con):
            con.close()

def sortingmovies():
    try:
        con = getconnection()
        cur = con.cursor()
        sql = "Select * from movies where rating > 6 order by rating desc;"
        cur.execute(sql)
        data = cur.fetchall()
        if(data != None):
            print("---The highest rated movies are---")
            for row in data:
                print(row)
    except sqlite3.Error as e:
        print("There is problem in sorting movies: ",e)
    finally:
        if(con):
            con.close()

ch = 1
while(ch!=4):
    print("~~~~WELCOME TO MOVIE MANAGER~~~~")
    print("1. Add movies", "2. Search Movies", "3. Info about latest trending movies", sep = "\n")
    ch = eval(input("Enter your choice:- "))
    if(ch == 1):
        Movie_name = input("Enter movie name: ")
        Movie_genre = input("Enter movie Genre: ")
        Movie_rating = input("Enter movie rating: ")
        data = (Movie_name, Movie_genre, Movie_rating)
        addmovies(data)
    elif(ch == 2):
        genre = input("Enter Genre of movie to search: ")
        if(searchmovies(genre)==True):
            print(genre)
    elif(ch == 3):
        sortingmovies()
    elif(ch==4):
        break;
