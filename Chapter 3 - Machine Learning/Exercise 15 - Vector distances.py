import numpy as np

x_train = np.random.rand(10, 3)   # generate 10 random vectors of dimension 3
x_test = np.random.rand(3)        # generate one more random vector of the same dimension

def dist(a, b):
    sum = 0
    for ai, bi in zip(a, b):
        sum = sum + (ai - bi)**2
    return np.sqrt(sum)
    
def nearest(x_train, x_test):
    nearest = 0
    min_distance = np.Inf
    x = 0
    min_distance = dist(x_test, x_train[0])
    for i in x_train:
        distance = dist(i, x_test)
        if distance < 0:
            abs(distance)
        if min_distance > distance:
            min_distance = distance
            nearest = x
        x+=1
            
    
    # add a loop here that goes through all the vectors in x_train and finds the one that
    # is nearest to x_test. return the index (between 0, ..., len(x_train)-1) of the nearest
    # neighbor
    print(nearest)

nearest(x_train, x_test)
