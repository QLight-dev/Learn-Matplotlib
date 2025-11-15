import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np 

# Make a diagonal line from 0,0 to 10,500
xpoints = np.array([0, 10])
ypoints = np.array([0, 500])

plt.plot(xpoints, ypoints)
plt.show()