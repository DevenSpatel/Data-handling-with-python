import sqlite3

def checkconnection():
    try:
        con = sqlite3.connect("C:\sqlite\Students.db")
        if(con):
            print("Connection fetched successfully!!")
            return con
    except sqlite3.Error as e:
            print("Problem in connecting with database: ",e)
            
def stud_login(Stud_id):
    try:
        con = checkconnection()
        cur = con.cursor()
        cur.execute("select Student_name, Position, Student_gpa from students_data where Student_id=?", (Stud_id,))
        data = cur.fetchone()
        if(data == None):
            print("Enter Valid Student ID")
            return False
        else:
            print("Welcome :", data[0])
            print("Your position in class is :", data[1])
            print("Your GPA is :", data[2])
            return True
    except sqlite3.Error as e:
        print("Problem in student login: ", e)
    finally:
        if(con):
            con.close()

def topper_students():
    try:
        con = checkconnection()
        cur = con.cursor()
        cur.execute("select Student_name, Student_gpa from students_data order by student_gpa desc limit 3")
        data = cur.fetchall()
        if(data == None):
            print("No Data Found")
            return False
        else:
            print("Top 3 Students are :")
            for row in data:
                print("Name: ", row[0], "GPA: ", row[1])
    except sqlite3.Error as e:
        print("Problem in fetching Data: ",e)
    finally:
        if(con):
            con.close()

Stud_id = int(input("Enter your Student Id to Check Result: "))
stud_login(Stud_id)
topper_students()
