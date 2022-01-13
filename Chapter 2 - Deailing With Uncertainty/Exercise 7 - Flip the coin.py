import numpy as np

def generate(p1):
    # change this so that it generates 10000 random zeros and ones
    # where the probability of one is p1
    seq = np.random.choice([0,1],p=[1-p1, p1], size=9996)
    return seq

def count(seq):
    amount = 0
    i = 0
    while i < len(seq):
        if seq[i:i+5].all():
            amount += 1
        i += 1
    return amount

def main(p1):
    seq = generate(p1)
    return count(seq)

print(main(2/3))
