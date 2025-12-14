# %%
import matplotlib

matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(170, 10, 250)

# %%
# Creating a Histogram
plt.hist(x)
plt.show()
