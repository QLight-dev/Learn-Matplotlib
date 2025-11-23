import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt 
import numpy as np 

# Markers
ypoints = np.array([1, 4, 2, 7, 5, 9, 5])
plt.plot(ypoints, marker= 'o')
plt.show()

# Format Strings
# Marker:line:color

plt.plot(ypoints, 'o:g')
plt.show()

# Marker Size
plt.plot(ypoints, marker = '*', ms = '30')
plt.show()

# Marker Colori
plt.plot(ypoints, marker = 'o', ms = 10, mec = 'g')