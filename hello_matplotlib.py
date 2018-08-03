import numpy as np # imports a fast numerical programming library
import scipy as sp # imports stats functions
import matplotlib as mpl 
import matplotlib.cm as cm # allows easy access to colormaps
import matplotlib.pyplot as plt # sets up plotting under plt
import pandas as pd # lets us handle data as dataframes
import seaborn as sns


x = np.linspace(0, 10, 30)  #array of 30 points from 0 to 10
y = np.tan(x)
z = y + np.random.normal(size=30) * .2
plt.plot(x, y, 'o-', label='A tangens wave')
plt.plot(x, z, '-', label='Noisy sine')
plt.legend(loc = 'lower right')
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.show()
