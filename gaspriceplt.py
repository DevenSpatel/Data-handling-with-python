import matplotlib.pyplot as plt
import numpy as np
import csv

#using csv module

def to_float(x):
    try:
        return float(x)
    except:
        return None
try:
    Year=[]
    Australia=[]
    Canada=[]
    France=[]
    Germany=[]
    Italy=[]
    Japan=[]
    Mexico=[]
    South_Korea=[]
    UK=[]
    USA=[]
    fobj = open('gas_prices.csv', 'r')
    reader = csv.reader(fobj)
    next(reader)
    for row in reader:
        Year.append(int(row[0]))
        Australia.append(to_float(row[1]))
        Canada.append(to_float(row[2]))
        France.append(to_float(row[3]))
        Germany.append(to_float(row[4]))
        Italy.append(to_float(row[5]))
        Japan.append(to_float(row[6]))
        Mexico.append(to_float(row[7]))
        South_Korea.append(to_float(row[8]))
        UK.append(to_float(row[9]))
        USA.append(to_float(row[10]))
except Exception as e:
    print("Error: ",e)
finally:
    if fobj != None:
        fobj.close()


plt.title("Gas prices over the years")
plt.plot(Year, USA, label= "USA", marker = "o", markersize = 5, linestyle = "--")
plt.plot(Year, South_Korea, label = "South Korea", color = "red", marker = "x", markersize = 5)
plt.plot(Year, Canada, label = "Canada", marker = "*", markersize = 5)
plt.xticks(Year[::3])
plt.xlabel("Year")
plt.ylabel("Gas Price in USD")
plt.legend()
plt.show()

#Another way of doing it 

Countries = [France, Germany, Italy, UK]
for country in Countries:
    if country in Countries:
        plt.plot(Year, country, marker = "o", markersize = 5)

plt.title("Gas price over the years")
plt.xlabel("Year")
plt.ylabel("Gas Price in USD")
plt.xticks(Year[::3])
plt.legend(["France", "Germany", "Italy", "UK"])    
plt.show()