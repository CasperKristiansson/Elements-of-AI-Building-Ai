import numpy as np
from io import StringIO


train_string = '''
25 2 50 1 500 127900
39 3 10 1 1000 222100
13 2 13 1 1000 143750
82 5 20 2 120 268000
130 6 10 2 600 460700
115 6 10 1 550 407000
'''

test_string = '''
36 3 15 1 850 196000
75 5 18 2 540 290000
'''

def main():
    np.set_printoptions(precision=1)

    data_train = np.genfromtxt(train, skip_header=1)
    data_test = np.genfromtxt(test, skip_header=1)

    x_train = data_train[:,:-1]
    y_train = np.asarray([])

    i = len(data_train) - 1
    while i >= 0:
        last_element = data_train[i][-1]
        y_train = np.insert(y_train, 0, last_element, axis = 0)
        i-=1

    x_test = data_test[:,:-1]

    coeff = np.linalg.lstsq(x_train, y_train)[0]

    print(coeff)
    print(x_test @ coeff)

train = StringIO(train_string)
test = StringIO(test_string)

main()
