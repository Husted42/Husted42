import numpy as np
from numpy import random

def weightedProb():
    X = ['a', 'b', 'c']
    P = [0.2, 0.3, 0.5]
    return np.random.choice(X, p=P)

def monteCarloCheck():
    a, b, c = 0, 0, 0
    for i in range (0, 1000):
        res = weightedProb()
        if res == 'a': a += 1
        elif res == 'b': b += 1
        else: c += 1
    sum = a+b+c
    return a/sum, b/sum, c/sum

print(monteCarloCheck())