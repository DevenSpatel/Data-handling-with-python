import csv

try:
    fobj = open("Student-data.csv", "r", newline = "\n")
    cwreader = csv.reader(fobj)
    
    header = next(cwreader)
    print("Rollno, Name, Subject1, Subject2, Subject3, Subject4, Subject5, total, Percentage")

    highest_total = -1

    for row in cwreader:
        rollno = row[0]
        name = row[1]
        s1 = int(row[2])
        s2 = int(row[3])
        s3 = int(row[4])
        s4 = int(row[5])
        s5 = int(row[6])

        total = s1+s2+s3+s4+s5
        percentage = (total/500)*100
        print(f"{rollno},{name},{s1},{s2},{s3},{s4},{s5},{total},{percentage:.2f}%")
        if total > highest_total:
            highest_total = total
            topper_name = name
            topper_rollno = rollno
    print(f"topper is {topper_name} with rollno {topper_rollno} having total marks {highest_total}")
except Exception as ex:
    print("Error in reading data: ", ex)
finally:
    if(fobj!=None):
        fobj.close()