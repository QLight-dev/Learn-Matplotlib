# %%
import matplotlib

matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import numpy as np

# %%
# Creating Bars
x = np.array(["Chocolate", "Vanilla", "Peppermint", "Mango"])
y = np.array([18, 12, 5, 10])
plt.bar(x, y)
plt.title("A survey of people's favourite icecreams")
plt.show()

# %%
# Horizontal Bars
x = np.array(["With black hair", "Without black hair"])
y = np.array([7, 23])
plt.barh(x, y)
plt.show()
