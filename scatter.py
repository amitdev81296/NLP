import matplotlib.pyplot as plt

# X coordinate representing sale of iced coffees
X = [590,540,740,130,810,300,320,230,470,620,770,250]

# Y coordinate representing temperature in Fahrenheit
Y = [32,36,39,52,61,72,77,75,68,57,48,48]

# Plots the graph with the coordinate lists
plt.scatter(X, Y, s=60, c='red', marker='^')

# Sets the graph title
plt.title('Relationship Betweem Temperature and Iced Coffee Sales')

# Sets labels for X and Y axes
plt.xlabel('Cups of Iced Coffee Sold')
plt.ylabel('Temperature in Fahrenheit')

# Opens the window where plot is displayed
plt.show()
