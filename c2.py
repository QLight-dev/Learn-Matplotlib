import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt 
import numpy as np

# Plotting x and y points 
xpoints = np.array([1, 6])
ypoints = np.array([4, 11])

plt.plot(xpoints, ypoints)
plt.show()

# Plotting without Line
xpoints = np.array([1, 6])
ypoints = np.array([4, 11])

plt.plot(xpoints, ypoints, "o")
plt.show()

# Multiple Points
xpoints = np.array([0, 3, 6, 9, 7, 6, 2, 8])
ypoints = np.array([0, 2, 4, 6, 7, 8, 3, 5])

plt.plot(xpoints, ypoints)
plt.show()