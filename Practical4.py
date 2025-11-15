# -*- coding: utf-8 -*-
"""
Created on Tue Aug  5 14:03:47 2025

@author: deven
"""

import sqlite3

def getconnection():
    try:
        con = sqlite3.connect("C:\sqlite\myphone.db")
        if(con):
            print("You're connected with Database!!")
        return con
    except sqlite3.Error as e:
        print("Problem in getting connected with database",e)
        
def displayall():
    try:
        con = getconnection()
        cur = con.cursor()
        sql = "select * from contacts"
        cur.execute(sql)
        data = cur.fetchall()
        for row in data:
            print(row)
    except sqlite3.Error as e:
            print("Problem in displaying your data!",e)
    finally:
            if(con):
                con.close()

def updatedata(data):
    try:
        con = getconnection()
        cur = con.cursor()
        sql = "update contacts set contact_name=:contact_name,contact_number=:contact_number,contact_email=:contact_email where contact_id=:contact_id"
        if(cur.execute(sql,data)):
            print("Contact data is updated!!")
        cur.close()
        con.commit()
    except sqlite3.Error as e:
        print("Problem in updating contact data",e)
    finally:
        if(con):
            con.close()

def deletedata(contact_id):
    try:
        con = getconnection()
        cur = con.cursor()
        sql = "Delete from contacts where contact_id=?"
        if(cur.execute(sql,(contact_id,))):
            print("Data deleted")
        con.commit()
    except sqlite3.Error as e:
        print("Problem in deleting data",e)
    finally:
        if(con):
            con.close()
            
def insertdata(data):
    try:
        con = getconnection()
        cur = con.cursor()
        sql = "insert into contacts(contact_name, contact_number, contact_email) values(?,?,?)"
        if(cur.execute(sql,data)):
            print("Your data is successfully inserted!!")
        cur.close()
        con.commit()
    except sqlite3.Error as e:
        print("Problem while inserting data",e)
    finally:
        if(con):
            con.close()

def getuserdata(contact_id):
    try:
        con = getconnection()
        cur = con.cursor()
        sql = "select * from contacts where contact_id=?"
        cur.execute(sql,(contact_id,))
        data = cur.fetchone()
        if(data!=None):
            print(data)
            print("Name :",data[1],"Email:",data[3],"Contact no:",data[2],sep="\n")
        else:
            print("Invalid contact")
            return False
        cur.close()
        return True
    except sqlite3.Error as e:
        print("Problem in getting user data",e)
    finally:
        if(con):
            con.close()
            
ch=1
while(ch!=6):
    print("1.Insert","2.Update","3.Delete","4.Select","5.SelectAll","6.Exit",sep="\n")
    ch=eval(input("Enter your choice:- "))
    if(ch==1):
        contact_name = input("Enter contact name:- ")
        contact_number = input("Enter contact number:- ")
        contact_email = input("Enter contact email:- ")
        data=(contact_name,contact_number,contact_email)
        insertdata(data)
    elif(ch==2):
        contact_id=eval(input("Enter contact id to update:- "))
        if(getuserdata(contact_id)==True):
            contact_name = input("Enter contact name:- ")
            contact_number = input("Enter contact number:- ")
            contact_email = input("Enter contact email:- ")
            data ={"contact_name":contact_name,"contact_number":contact_number,"contact_email":contact_email,"contact_id":contact_id}
            updatedata(data)
    elif(ch==3):
        contact_id=eval(input("Enter contact_id to delete:- "))
        if(getuserdata(contact_id)==True):
            deletedata(contact_id)
    elif(ch==4):
        contact_id=eval(input("Select contact id:- "))
        if(getuserdata(contact_id)==True):
                    print(contact_id)
    elif(ch==5):
        displayall()
            
            
            
        
            
        
























    
    
    
    