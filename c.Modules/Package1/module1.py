## MODULE 1: It will have some functions

import numpy as np
import matplotlib.pyplot as plt

print('This is being run')

def plot(x,y):
    A = plt.figure()
    plt.plot(x,y)
    plt.show()
    return A