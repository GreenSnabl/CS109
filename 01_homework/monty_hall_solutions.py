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

# this is the given solution, which 

def simulate_prizedoor(nsim):
    return np.random.randint(0, 3, (nsim))

def simulate_guess(nsim):
        return np.zeros(nsim, dtype=np.int)

def goat_door(prizedoors, guesses):
        
        #strategy: generate random answers, and
        #keep updating until they satisfy the rule
        #that they aren't a prizedoor or a guess
        result = np.random.randint(0, 3, prizedoors.size)
        while True:
            bad = (result == prizedoors) | (result == guesses)
            if not bad.any():
                return result
            result[bad] = np.random.randint(0, 3, bad.sum())

def switch_guess(guesses, goatdoors):
    result = np.zeros(guesses.size)
    switch = {(0, 1): 2, (0, 2): 1, (1, 0): 2, (1, 2): 1, (2, 0): 1, (2, 1): 0}
    for i in [0, 1, 2]:
        for j in [0, 1, 2]:
            mask = (guesses == i) & (goatdoors == j)
            if not mask.any():
                continue
            result = np.where(mask, np.ones_like(result) * switch[(i, j)], result)
            return result

def win_percentage(guesses, prizedoors):
    return 100 * (guesses == prizedoors).mean()


nsim = 10000

#keep guesses
print "Win percentage when keeping original door"
print win_percentage(simulate_prizedoor(nsim), simulate_guess(nsim))

#switch
pd = simulate_prizedoor(nsim)
guess = simulate_guess(nsim)
goats = goat_door(pd, guess)
guess = switch_guess(guess, goats)
print "Win percentage when switching doors"
print win_percentage(pd, guess).mean()
