# -*- coding: utf-8 -*-
"""
Created on Tue Aug 19 19:19:04 2025

@author: deven
"""

import sqlite3

def getconnection():
    try:
        con = sqlite3.connect("C:/sqlite/user.db")
        if(con):
            print("...")
        return con
    except sqlite3.Error as e:
        print("Problem in connecting with database",e)

def checklogin(user_email, user_passsword, user_contact):
    try:
        con = getconnection()
        cur = con.cursor()
        cur.execute("select user_name, user_contact, user_passsword from users where user_email=?",(user_email,))
        data = cur.fetchone()
        if(data==None):
            print("User is not registered")
            return False
        usrcontact=data[1]
        if(usrcontact!=user_contact):   
            print("There is no such contacts!")
            return False
        passworddb=data[2]
        if(passworddb==user_passsword):
            print("Welcome back ",data[0])
            return True
        else:
            print("Invalid password!")
            return False
            
    except sqlite3.Error as e:
        print("There is problem in login:- ", e)
    finally:
        if(con):
            con.close()
            
email = input("Enter your email:- ")
contact = int(input("Enter your contact:- "))
password = input("Enter your password:- ")
checklogin(email, password, contact)
    
        
            
        
    
        
        