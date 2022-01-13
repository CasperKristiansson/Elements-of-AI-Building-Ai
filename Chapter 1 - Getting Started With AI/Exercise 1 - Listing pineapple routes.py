#### TEST
portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]
def permute(route, ports):
    i = 0
    for j in range(1, 5):
        for k in range(1, 5):
            for l in range(1, 5):
                for m in range(1, 5):
                    route = [j, k, l, m]

                    if all(elem in route for elem in ports):
                        route = [i, j, k, l, m]
                        print(' '.join([portnames[i] for i in route]))

permute([0], list(range(1, len(portnames))))

#### SVAR
def permutations(route, ports):
    if len(ports) < 1:
        print(' '.join([portnames[i] for i in route]))
    else:
        for i in range(len(ports)):
            permutations(route+[ports[i]], ports[:i]+ports[i+1:])
 
permutations([0], list(range(1, len(portnames))))