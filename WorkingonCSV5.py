import csv
import os

try:
    if os.path.exists("Student-data.csv"):
        fobj = open("Student-data.csv", "w", newline = "\n")
    else:
        fobj = open("Student-data.csv", "w", newline = "\n")
    if(fobj!=None):
        header = ['Rollno', 'Name', 'Subject1', 'Subject2', 'Subject3', 'Subject4', 'Subject5']
        cwriter = csv.DictWriter(fobj, fieldnames = header)
        if(fobj.mode == 'w'):
            cwriter.writeheader()
        ch = 'y'
        while(ch=='y' or ch=="Y"):
            rollno = input("Enter Roll Number:- ")
            name = input("Enter Name:- ")
            subject1 = input("Enter Subject1 Marks:- ")
            subject2 = input("Enter Subject2 Marks:- ") 
            subject3 = input("Enter Subject3 Marks:- ")
            subject4 = input("Enter Subject4 Marks:- ")
            subject5 = input("Enter Subject5 Marks:- ")
            row = {'Rollno': rollno, 'Name': name, 'Subject1': subject1, 'Subject2': subject2, 
                   'Subject3': subject3, 'Subject4': subject4, 'Subject5': subject5}
            cwriter.writerow(row)
            ch = input("Do you want to add more records (y/n):- ")
except Exception as ex:
    print("Error in writing data: ",ex)
finally:
    if (fobj!=None):
        fobj.close()
