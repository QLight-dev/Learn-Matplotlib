import matplotlib

matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import numpy as np

# Draw multiple plots in one Figure
# Plot 1
x = np.array([0, 1, 2, 3])
y = np.array([2, 8, 1, 10])

# One row, two columns, 1st plot
plt.subplot(1, 2, 1)
plt.plot(x, y)

# Plot 2
x = np.array([0, 1, 2, 3])
y = np.array([80, 90, 100, 110])

# One row, two columns, 2nd plot
plt.subplot(1, 2, 2)
plt.plot(x, y)

plt.show()

# Add title
# Plot 1
x = np.array([0, 1, 2, 3])
y = np.array([2, 8, 1, 10])

plt.subplot(1, 2, 1)
plt.title("Plot 1")
plt.plot(x, y)

# Plot 2
x = np.array([0, 1, 2, 3])
y = np.array([80, 90, 100, 110])

plt.subplot(1, 2, 2)
plt.title("Plot 2")
plt.plot(x, y)

plt.show()

# Super title

x = np.array([0, 1, 2, 3])
y = np.array([2, 8, 1, 10])

plt.subplot(1, 2, 1)
plt.title("Plot 1")
plt.plot(x, y)

# Plot 2
x = np.array([0, 1, 2, 3])
y = np.array([80, 90, 100, 110])

plt.subplot(1, 2, 2)
plt.title("Plot 2")
plt.plot(x, y)

plt.suptitle("Full plot (its so high)")
plt.show()

