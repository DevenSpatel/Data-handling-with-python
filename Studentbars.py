import matplotlib.pyplot as plt
import numpy as np
import csv

try:
    Name = []
    Maths = []
    Science = []
    English = []
    Computer = []
    fobj = open('Students-marks.csv', 'r')
    reader = csv.reader(fobj)
    next(reader)
    for row in reader:
        Name.append(row[1])
        Maths.append(int(row[2]))
        Science.append(int(row[3]))
        English.append(int(row[4]))
        Computer.append(int(row[5]))
except Exception as e:
    print("Error while loading the data: ", e)
finally:
    if fobj != None:
        fobj.close()

# Maths bar chart
bars = plt.bar(Name, Maths, label = "Maths")
plt.title("Students Marks difference in maths")
plt.xlabel("Students Name")
plt.ylabel("Marks in Maths")
plt.xticks(rotation=45)
plt.yticks(np.arange(0, 101, 10))
bars[7].set_hatch('/')
plt.legend()
plt.show()

# Science bar chart
bars = plt.bar(Name, Science, color = "Green", label = "Science")
plt.title("Students Marks Difference in Science")
plt.xlabel("Students Name")
plt.ylabel("Marks in Science")
plt.xticks(rotation = 45)
plt.yticks(np.arange(0,101,10))
bars[7].set_hatch("\\")
plt.legend()
plt.show()

# English Bar chart
bars = plt.bar(Name, English, color = "Orange", label = "English")
plt.title("Students marks difference in english")
plt.xlabel("Students Name")
plt.ylabel("Marks in English")
plt.xticks(rotation = 45)
plt.yticks(np.arange(0,101,10))
bars[7].set_hatch("*")
plt.legend()
plt.show()

# Computer bar chart
bars = plt.bar(Name, Computer, color = "red", label = "Computer")
plt.title("Students Marks Difference in computer", style = "oblique")
plt.xlabel("Students Name")
plt.ylabel("Marks in Computer")
plt.xticks(rotation = 45)
plt.yticks(np.arange(0,101,10))
bars[7].set_hatch("o")
plt.legend()
plt.show()

# combined bar chart maths and science
n = len(Name)
x = np.arange(n)
bar_width = 0.3
plt.figure(figsize=(12,8))
plt.bar(x - bar_width/2, Maths, width = bar_width, label = "Maths", color = "blue")
plt.bar(x + bar_width/2, Science, width = bar_width, label = "Science", color = "green")
plt.title("Students marks comparison in Maths and Science", fontweight = "bold")
plt.xlabel("Students Name", fontweight = "bold")
plt.ylabel("Marks obtained", fontweight = "bold")
plt.xticks(x, Name, rotation = 45)
plt.yticks(np.arange(0,101,10))
plt.legend()
plt.show()

# Combined bar chart English and Computer
n = len(Name)
x = np.arange(n)
bar_width = 0.3
plt.figure(figsize=(12,8))
plt.bar(x - bar_width/2, English, width = bar_width, label = "English", color = "orange")
plt.bar(x + bar_width/2, Computer, width = bar_width, label = "Computer", color = "red")
plt.title("Students marks comparison in English and Computer", fontweight = "bold")
plt.xlabel("Students Name", fontweight = "bold")
plt.ylabel("Marks obtained", fontweight = "bold")
plt.xticks(x, Name)
plt.yticks(np.arange(0,101,10))
plt.legend()
plt.show()

#Overall marks comparison and highest,lowest scorer
n = len(Name)
x = np.arange(n)
bar_width = 0.2
plt.figure(figsize = (15,8))
bars1 = plt.bar(x - 1.5*bar_width, Maths, width = bar_width, label = "Maths", color = "blue")
bars2 = plt.bar(x - 0.5*bar_width, Science, width = bar_width, label = "Science", color = "green")
bars3 = plt.bar(x + 0.5*bar_width, English, width = bar_width, label = "English", color = "orange")
bars4 = plt.bar(x + 1.5*bar_width, Computer, width = bar_width, label = "Computer", color = "red")
plt.title("Overall Marks comparison", fontweight = "bold")
plt.xlabel("Students Name", fontweight = "bold")
plt.ylabel("Marks obtained", fontweight = "bold")
plt.xticks(x, Name, style = "italic", fontweight = "bold")
plt.yticks(np.arange(0,101,10))
bars1[7].set_hatch('/')
bars2[7].set_hatch('\\')
bars3[7].set_hatch('*')
bars4[7].set_hatch('o')
plt.legend()
plt.show() 

# horizontal bar charts
n = len(Name)
y = np.arange(n)
bar_height = 0.2
plt.figure(figsize = (15,8))
bars1 = plt.barh(y - 1.5*bar_height, Maths, height = bar_height, label = "Maths", color = "blue")
bars2 = plt.barh(y - 0.5*bar_height, Science, height = bar_height, label = "Science", color = "green")
bars3 = plt.barh(y + 0.5*bar_height, English, height = bar_height, label = "English", color = "orange")
bars4 = plt.barh(y + 1.5*bar_height, Computer, height = bar_height, label = "Computer", color = "red")
plt.title("Overall Marks comparison - Horizontal Bar Chart", fontweight = "bold")
plt.ylabel("Students Name", fontweight = "bold")
plt.xlabel("Marks obtained", fontweight = "bold")
plt.yticks(y, Name, style = "italic", fontweight = "bold")
plt.xticks(np.arange(0,101,10))
bars1[7].set_hatch('/')
bars2[7].set_hatch('\\')
bars3[7].set_hatch('*')
bars4[7].set_hatch('o')
plt.legend()
plt.show()