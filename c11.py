# %%
import matplotlib

matplotlib.use("TkAgg")

# %%
import matplotlib.pyplot as plt
import numpy as np

# %%
# Create variables
y = np.array([15, 28, 32, 14, 11])
labels = ["These", "Are", "Some", "Odd", "Labels"]
theExplode = [0.3, 0.1, 0.0, 0.2, 0.0]
colors = ["red", "orange", "y", "#00ff00"]

# %%
# Creating Pie Charts
plt.pie(y)
plt.show()

# %%
# Adding Labels
plt.pie(y, labels=labels)
plt.show()

# %%
# Change Start Angle
plt.pie(y, labels=labels, startangle=23)
plt.show()

# %%
# Make the wedges stand out (explode)
plt.pie(y, labels=labels, startangle=23, explode=theExplode)
plt.show()

# %%
# Add Shadow
plt.pie(y, labels=labels, startangle=23, explode=theExplode, shadow=True)
plt.show()

# %%
# Choose color for each one
plt.pie(y, labels=labels, startangle=23, explode=theExplode, shadow=True, colors = colors)
plt.show()

# %%
# Add a Legend
plt.pie(y, labels=labels, startangle=23, explode=theExplode, shadow=True, colors = colors)
plt.legend()
plt.show()

# %%
# Add a legend title
plt.pie(y, labels=labels, startangle=23, explode=theExplode, shadow=True, colors = colors)
plt.legend(title = "Well...")
plt.show()
