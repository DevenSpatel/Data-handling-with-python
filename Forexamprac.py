import csv 
import os

try:
    if os.path.exists("Student-data.csv"):
        fobj = open("Student-data.csv", "a", newline = "\n")
    else:
        fobj = open("Student-data.csv", "w", newline = "\n")
    if(fobj!=None):
        header = ["Rollno", "Name"]
        cwriter = csv.DictWriter(fobj, fieldnames = header)
        if(fobj.mode == 'w'):
            cwriter.writeheader()
        ch = 'y'
        while(ch=='y' or ch=="Y"):
            rollno = input("Enter Roll Number:- ")
            name = input("Enter Name:- ")
            row = {'Rollno': rollno, 'Name': name}
            cwriter.writerow(row)
            ch = input("Do you want to add more records? (y/n):-  ")
except Exception as ex:
    print("Error in writing data: ",ex)
finally:
    if(fobj!=None):
        fobj.close()