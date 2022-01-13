portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]

# https://sea-distances.org/
# nautical miles converted to km

smallest = 1000000
bestroute = [0, 0, 0, 0, 0]
D = [
    [0,8943,8019,3652,10545],
    [8943,0,2619,6317,2078],
    [8019,2619,0,5836,4939],
    [3652,6317,5836,0,7825],
    [10545,2078,4939,7825,0]
]

# https://timeforchange.org/co2-emissions-shipping-goods
# assume 20g per km per metric ton (of pineapples)

co2 = 0.020

# DATA BLOCK ENDS

# these variables are initialised to nonsensical values
# your program should determine the correct values for them


def permutations(route, ports):
    global smallest, bestroute
    # write the recursive function here
    # remember to calculate the emissions of the route as the recursion ends
    # and keep track of the route with the lowest emissions
    if len(ports) < 1:
        shortest = 1000000
        count = D[0][route[1]]
        count += D[route[1]][route[2]]
        count += D[route[2]][route[3]]
        count += D[route[3]][route[4]]
        if count < smallest:
            smallest = count
            bestroute = route
    else:
        for i in range(len(ports)):
            permutations(route+[ports[i]], ports[:i]+ports[i+1:])

    pass

def main():
    global smallest
    # this will start the recursion 
    permutations([0], list(range(1, len(portnames))))
    smallest = smallest*co2
    # print the best route and its emissions
    print(' '.join([portnames[i] for i in bestroute]) + " %.1f kg" % smallest)

main()
