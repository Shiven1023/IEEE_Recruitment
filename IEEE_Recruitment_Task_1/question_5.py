import numpy as np
import matplotlib.pyplot as plt
arr = np.random.normal(loc = 0,scale = 1,size = 1000)
plt.scatter(range(1000),arr,alpha = 0.6)
plt.title("ScatterPlot of 1000 Random Numbers")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.plot()