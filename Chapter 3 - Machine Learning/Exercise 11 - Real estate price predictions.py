# input values for three mökkis: size, size of sauna, distance to water, number of indoor bathrooms, 
# proximity of neighbors
X = [[66, 5, 15, 2, 500], 
     [21, 3, 50, 1, 100], 
     [120, 15, 5, 2, 1200]]
c = [3000, 200, -50, 5000, 100]    # coefficient values

def predict(X, c):
    price = 0 
    for cabin in X:
        for coefficient in c:
            price += cabin[c.index(coefficient)]*coefficient
        print(price)
        price = 0
               
predict(X, c)