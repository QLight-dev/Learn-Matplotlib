import matplotlib

matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import numpy as np

# Matplotlib Addding Grid Lines

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

# Add Grid Lines to a Plot
plt.plot(x, y)

plt.title("Sports Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calories burnage")

plt.grid()
plt.show()

# Specify Which Grid Lines To Display
plt.plot(x, y)

plt.title("Sports Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calories burnage")

plt.grid(axis="y")
plt.show()

# Set Line Properties For Grid
plt.plot(x, y)

plt.title("Sports Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calories burnage")

plt.grid(color = 'green', linestyle = '--', linewidth = 1.5)
plt.show()
