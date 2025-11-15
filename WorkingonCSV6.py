import csv

try:
    fobj = open("Student-data.csv", "r", newline = "\n")
    cwreader = csv.reader(fobj)

    header = next(cwreader)
    print("Rollno, Name, Subject1, Subject2, Subject3, Subject4, Subject5, total, Percentage")

    higest_total = -1

    for row in cwreader:
        rollno = row[0]
        name = row[1]
        m1 = int(row[2])
        m2 = int(row[3])
        m3 = int(row[4]) 
        m4 = int(row[5])
        m5 = int(row[6])
        
        total = m1+m2+m3+m4+m5
        percentage = (total/500)*100
        print(f"{rollno},{name},{m1},{m2},{m3},{m4},{m5},{total},{percentage:.2f}%")

        if total > higest_total:
            highest_total = total
            topper_name = name
            topper_rollno = rollno
            
    print(f"topper is {topper_name} with rollno {topper_rollno} having total marks {highest_total}")

except Exception as ex:
    print("Error in reading data: ",ex)
finally:
    if(fobj!=None):
        fobj.close()