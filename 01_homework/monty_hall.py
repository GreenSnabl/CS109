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
    return np.random.randint(0, 3, nsim)

def simulate_guess(x):
    #guesses = []
    #for i in range (0, x):
    #    guesses.append((i + pow(3,i)) % 3)
    #return guesses
    return np.random.choice([1,2], x)

def goat_door(prizedoors, guesses):
    goat_doors = []    
    if (prizedoors.size != guesses.size):
        raise Exception("Size of prizedoors and guesses need to be the same")
    for i in range (0, guesses.size):
        possible = [0, 1, 2]
        if prizedoors[i] in possible:
            possible.remove(prizedoors[i])
        if guesses[i] in possible:
            possible.remove(guesses[i])
        goat_doors.append(np.random.choice(possible))
    return np.asarray(goat_doors)

def switch_guess(guesses, goatdoors):
    switch_doors = []    
    if (goatdoors.size != guesses.size):
        raise Exception("Size of prizedoors and guesses need to be the same")
    for i in range (0, guesses.size):
        possible = [0, 1, 2]
        if goatdoors[i] in possible:
            possible.remove(goatdoors[i])
        if guesses[i] in possible:
            possible.remove(guesses[i])
        switch_doors.append(np.random.choice(possible))
    return np.asarray(switch_doors)

def win_percentage(guesses, prizedoors):
    cnt = 0
    if (prizedoors.size != guesses.size):
        raise Exception("Size of prizedoors and guesses need to be the same")
    for i in range(0, guesses.size):
        if (prizedoors[i] == guesses[i]):
            cnt += 1
    return cnt / guesses.size



values = []
all_in_one = []
for i in range(100,100000, 10000):
    values.append((simulate_prizedoor(i), simulate_guess(i)))

for v in values:
    goat = goat_door(v[0], v[1])
    switch = switch_guess(v[1], goat)
    all_in_one.append((v[0], v[1], goat, switch))

for x in all_in_one:
#    print(np.asarray(x))
    print("Win percentage without switching: ", win_percentage(x[1], x[0]))
    print("Win percentage with switching: ", win_percentage(x[3], x[0]), "\n")
