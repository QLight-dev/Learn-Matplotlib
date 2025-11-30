import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt 
import numpy as np

ypoints = np.array([5, 7, 3, 2])

# Change style of line to dotted
print("Change style of line to be dotted")
plt.plot(ypoints, linestyle = "dotted")
plt.show()

# Change style of line to dashed
print("Change style of word to be dashed")
plt.plot(ypoints, linestyle = "dashed")
plt.show()

# Shorter Syntax for dashed
print("Shorter Syntax for dashed")
plt.plot(ypoints, ls = "--")
plt.show()

# Line Color
print("Line color")
plt.plot(ypoints, color = "g")
plt.show()

# use hexadecimal
print("Use Hexadecimal")
plt.plot(ypoints, c = "#3F7A9C")
plt.show()

# Line Width
# linewidth = lw
print("Change line width")
plt.plot(ypoints, lw = "15.8")
plt.show()

# Multiple Lines
print("Multiple Lines")
y_point1 = np.array([2, 5, 7, 3])
y_point2 = np.array([9, 3, 7, 2])

plt.plot(y_point1)
plt.plot(y_point2)
plt.show()