import math
import numpy as np

x = np.array([4, 3, 0])
c1 = np.array([-.5, .1, .08])
c2 = np.array([-.2, .2, .31])
c3 = np.array([.5, -.1, 2.53])

def sigmoid(c1):
    # add your implementation of the sigmoid function here
    test = sum(c1)
    print(test)

# calculate the output of the sigmoid for x with all three coefficients

sigmoid(c3)