# See all the "as ..." contructs? They're just aliasing the package names.
# That way we can call methods like plt.plot() instead of matplotlib.pyplot.plot().

import numpy as np # imports a fast numerical programming library
import scipy as sp #imports stats functions, amongst other things
import matplotlib as mpl # this actually imports matplotlib
import matplotlib.cm as cm #allows us easy access to colormaps
import matplotlib.pyplot as plt #sets up plotting under plt
import pandas as pd #lets us handle data as dataframes
#sets up pandas table display
pd.set_option('display.width', 500)
pd.set_option('display.max_columns', 100)
pd.set_option('display.notebook_repr_html', True)
import seaborn as sns #sets up styles and gives us more plotting options

print ("Make a 3 row x 4 column array of random numbers")
x = np.random.random((3, 4))
print (x)
print ()

print ("Add 1 to every element")
x = x + 1
print (x)
print()

print ("Get the element at row 1, column 2")
print (x[1, 2])
print()

# The colon syntax is called "slicing" the array. 
print ("Get the first row")
print (x[0, :])
print()

print ("Get every 2nd column of the first row")
print (x[0, ::2])
print()

print("Get the first two elements of the second row")
print(x[1, :2])
print()

print ("Max is: %f" % x.max())
print ("Min is: %f" % x.min())
print ("Mean is: %f\n" % x.mean())

print("Max of axis=1, means maximum value in each row")
print(x.max(axis=1))
print("Min of axis=1, same as above")
print(x.min(axis=1))
print()


print("Max of axis=0, means maximum value in each col")
print(x.max(axis=0))
print("Min of axis=0, same as above")
print(x.min(axis=0))
print()
                                        # Wahrscheinlichkeitsdichte der Binomialverteilung
                                        # P(N) = (n over N) * p^N(1-P)^(n-N)
                                        # np.random.binomial(n, p, size=None)
x = np.random.binomial(500, .5, 500)    # Flipping a coin 500 times, getting number of heads
print("number of heads:", x)            # repeating the procedure 500 times


plt.hist(x, 10)     # create the histogram, hist(data, bins=none, range=none, density=none,
                    #   weights=none, cumulative=False,....)
plt.show()
