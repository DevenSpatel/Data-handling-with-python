import sqlite3

def getconnection():
    try:
        con = sqlite3.connect("C:/sqlite/user.db")
        if(con):
            print("You are connected with database!!")
        return con
    except sqlite3.Error as e:
        print("There is problem in connecting with database: ",e)

def checklogin(user_email, user_contact, user_passsword):
    try:
        con = getconnection()
        cur = con.cursor()
        cur.execute("Select user_name, user_contact, user_passsword from users where user_email=?", (user_email,))
        data = cur.fetchone()
        if(data == None):
            print("User is not registered!")
            return False
        usrcontact=data[1]
        if(usrcontact!=user_contact):
            print("There is no such contact")
            return False
        usrpassword=data[2]
        if(usrpassword==user_passsword):
            print("Welcome back ",data[0])
            return True
        else:
            print("Invalid password!!")
            return False
    except sqlite3.Error as e:
        print("There is problem in verifying your data: ",e)
    finally:
        if(con):
            con.close()
            
email=input("Enter your email: ")
number=eval(input("Enter your number: "))
password=input("Enter your password: ")
checklogin(email, number, password)