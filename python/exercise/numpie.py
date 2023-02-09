import numpy as np
a = np.array([1,2,3])

def intoArray ():
    print("----- Introduction to arrays in numpy -----")
    a = np.array([1,2,3,4])
    b = np.array([1,2,3,4], float)
    c = np.array((1,2,3,4))
    print (str(a)+ " " +str(b)+ " " +str(c))
    print("Arrange:    " + str(np.arange(2.0, 2.4, 0.1)))
    print("Zeros/Ones: " + str(np.zeros(4)) + str(np.ones(4)))
    print("Calculations:")
    print(a)
    print(3*a)
    print(a+a)
    print(a*a)
    print(a/a)
    print(np.cos(a))
    print("Random arrays:")
    print(np.random.rand(3))
    print(np.random.rand(3,5))
    print(np.random.randint(1,3,5))
    print("")

def multiArray ():
    print("----- Multidimensional arrays -----")
    a = np.array([[1,2,3,4], [2,3,4,5]])
    print(a)
    print("shape:" + str(a.shape))

def e1 ():
    print("----- Exercise 1 -----")
    c = np.average( np.random.randint(1,7,10000) + np.random.randint(1,7,10000) )
    print (c)
    print ("")

def run ():
    if (True): intoArray()
    if (False): e1()
    if (True): multiArray()
run()