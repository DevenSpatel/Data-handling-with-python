import matplotlib.pyplot as plt
import numpy as np

# My first Plot in matplotlib
'''x = [2,3,5,7]
y = [7,9,10,12]
x2 = np.array([1,2.3,4.8])
plt.plot(x2, x2**2, label = "x Squared", color = "green", linestyle = "--", marker = "o", markersize = 5)
plt.title("My First plot")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.plot(x,y, label = "Line", color = "r", marker = "o", markersize = 10)
plt.xticks([0,2,4,6,8,10,12,14,16])
plt.yticks([0,2,4,6,8,10,12,14,16])
plt.legend()
plt.show()  ''' 

# bar Charts
labels = ['A', 'B', 'C', 'D']
values = [10, 20, 5, 40]
bars = plt.bar(labels, values, color = "purple", label = "/ - bar1, o - bar2, * - bar3, \\ - bar4")
bars[0].set_hatch('/')
bars[1].set_hatch('o')
bars[2].set_hatch('*')
bars[3].set_hatch('\\')
plt.title("First Bar chart")
plt.legend()
plt.show()