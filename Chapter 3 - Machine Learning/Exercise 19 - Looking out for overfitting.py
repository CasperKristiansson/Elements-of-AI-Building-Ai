from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
import numpy as np

# do not edit this
# create fake data
x, y = make_moons(
    n_samples=500,  # the number of observations
    random_state=42,
    noise=0.3
)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)
print(x_train)
# Create a classifier and fit it to our data
knn = KNeighborsClassifier(n_neighbors=133)
knn.fit(x_train, y_train)

y_predict = np.empty(len(y_test), dtype=np.int64)

lines = []

def dist(a, b):
    sum = 0
    for ai, bi in zip(a, b):
        sum = sum + (ai - bi)**2
    return np.sqrt(sum)

def main(X_train, X_test, y_train, y_test):
    global y_predict
    global lines
    k = 3

    for i, test_item in enumerate(X_test):

        distances = [dist(train_item, test_item) for train_item in X_train]
        nearest_indices = np.argsort(distances)
        nearest_labels = y_train[nearest_indices[:k]]


        y_predict[i] = np.round(np.mean(nearest_labels))
    print(y_predict)

main(x_train, y_train, x_test, y_test)

print("training accuracy: %f" % 0.0)
print("testing accuracy: %f" % 0.0)
