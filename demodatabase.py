# -*- coding: utf-8 -*-
"""
Created on Wed Jul 23 09:35:13 2025

@author: Pritesh
"""
import sqlite3

#function to connectwith database
def getconnection():
    try:
        con = sqlite3.connect("C:\sqlite\college.db")
        if(con):
            print("Data base connected")
        return con
    except sqlite3.Error as e:
        print(" Problem in getconnection ",e)
        
#function to getdata from database
def displayall():
    try:
        con = getconnection()
        cur = con.cursor()
        sql = "select * from contacts"
        cur.execute(sql)
        data = cur.fetchall()
        print(" type of data ",type(data))
        for row in data:
            print(row)
    except sqlite3.Error as e:
        print(" Problem in displayall ",e)
    finally:
        if(con):
            con.close()
#function to update data
def updatedata(data):
    try:
        con = getconnection()
        cur = con.cursor()
        sql = "update contacts set con_name=:con_name,con_num=:con_num,con_email=:con_email where con_id=:con_id"
        if(cur.execute(sql,data)):
            print("contact data updated")
        cur.close()
        con.commit()
    except sqlite3.Error as e:
        print("problem in updatedata:-",e)
    finally:
        if(con):
            con.close()
            
#functon to delete data
def deletedata(con_id):
    try:
        con = getconnection()
        cur = con.cursor()
        sql = "delete from contacts where con_id=?"
        if(cur.execute(sql,(con_id,))):
            print("data Deleted")
        cur.close()
        con.commit()
    except sqlite3.Error as e:
        print("Problem in deletedata :-",e)
    finally:
        if(con):
            con.close()
    
            
#function to insert data 
def insertdata(data):
    try:
        con = getconnection()
        cur = con.cursor()
        sql = "insert into contacts(con_name,con_num,con_email)values(?,?,?)"
        if(cur.execute(sql,data)):
            print("data inserted")
        cur.close()
        con.commit()
    except sqlite3.Error as e:
        print(" Problem in insertdata :-",e)
    finally:
        if(con):
            con.close()
#function to get single user data
def getuserdata(con_id):
    try:
        con = getconnection()
        cur = con.cursor()
        sql = "select * from contacts where con_id=?"
        cur.execute(sql,(con_id,))
        data = cur.fetchone()
        if(data!=None):
            print(data)
            print("Name :",data[1],"Email:",data[3],"Contact no:",data[2],sep="\n")
        else:
            print("invalid contact")
            return False
        cur.close()
        return True
    except sqlite3.Error as e:
        print("problem in getuserdata :-",e)
    finally:
        if(con):
            con.close()
ch=1
while(ch!=6):
    print("1.Insert","2.Update","3.Delete","4.Select","5.SelectAll","6.Exit",sep="\n")
    ch=eval(input("enter your Choice:-"))
    if(ch==1):
        con_name = input("Enter Conatct Name:-")
        con_num = input("Enter Contact Number:-")
        con_email = input("Enter Contact Email:-")
        data = (con_name,con_num,con_email)
        insertdata(data)
    elif(ch==2):
        con_id=eval(input("Enter con_id to update:-"))
        if(getuserdata(con_id)==True):
            con_name = input("Enter Conatct Name:-")
            con_num = input("Enter Contact Number:-")
            con_email = input("Enter Contact Email:-")
            #data = (con_name,con_num,con_email)
            data = {"con_num":con_num,"con_name":con_name,"con_email":con_email,"con_id":con_id}
            updatedata(data)
    elif(ch==3):
        con_id=eval(input("Enter con_id to Delete:-"))
        if(getuserdata(con_id)==True):
            deletedata(con_id)
    elif(ch==5):
        displayall()
        
    
 




