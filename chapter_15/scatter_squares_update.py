#Gabriel Abraham
#notesonartificialintelligence
#Python Crash Course - Project 2 - Chapter 15

import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]
y_values = [1 , 4, 9, 16, 25]

plt.style.use("seaborn")
fig, ax = plt.subplots()
ax.scatter(x_values,y_values, s = 100)

#Set Chart title and Label axes.
ax.set_title("Square Numbers", fontsize = 24)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Square of Value", fontsize = 14)

#Set size of tick labels.
ax.tick_params(axis = "both", which = "major", labelsize = 14)

plt.show()