import matplotlib

matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import numpy as np

# Matplotlib Labels and title

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

# Create Labels for a plot
plt.plot(x, y)
plt.xlabel("Average Pulse")
plt.ylabel("Calories burnage")
plt.show()

# Create title for a plot
plt.plot(x, y)
plt.title("Sports data")
plt.show()

# Set font properties
plt.plot(x, y)
plt.title("Sports data", fontdict = {'family':'serif','color':'green','size':40})
plt.xlabel("Average Pulse", fontdict =  {'family':'serif','color':'red','size':27})
plt.ylabel("Calories brunage", fontdict = {'family':'serif','color':'orange','size':18})
plt.show()

# Change the postion of the title
plt.plot(x, y)
plt.title("Sports Data", loc = 'right')
plt.show()
