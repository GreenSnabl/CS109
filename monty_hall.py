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


#   """
#   Function
#   --------
#   simulate_prizedoor
#   
#   Generate a random array of 0s, 1s, and 2s, representing
#   hiding a prize between door 0, door 1, and door 2
#   
#   Parameters
#   ----------
#   nsim : int
#       The number of simulations to run
#   
#       Returns
#       -------
#       sims : array
#           Random array of 0s, 1s, and 2s
#   
#           Example
#           -------
#           >>> print simulate_prizedoor(3)
#           array([0, 0, 2])
#           """
#           def simulate_prizedoor(nsim):
#                   #compute here
#                       return answer
#                   #your code here

def simulate_prizedoor(nsim):


    return answer

