##### -- Øvelse 1 -- #####
lst3 = ["Napoleon", "Wellington", "Bonaparte", "Wellington"]
lst4 = [1,2,3,4,5,1,5,4,3,2,1]

def forekomster (lst, x) :
    a = lst.count(x)
    print(a)

print("Øvelse 1 ")
forekomster(lst3, "Wellington")
forekomster(lst4, 1)

##### -- Øvelse 2 -- #####
print()
print("Øvelse 2 ")
def palindrom (word):
    txt = word [::-1]
    if word == txt:
        return True
    else:
        return False

print (palindrom("ebbe"))
print (palindrom("jens"))

##### -- Øvelse 3 -- #####
print()
print("Øvelse 3 ")

##### -- 2ø0 -- #####
print("2ø0")
def nul() :
    firstName = "Jon"
    lastName = "Sporring"
    print(firstName, lastName)
nul()

##### -- 2ø1 -- #####
print( )
print("2ø1")
def en (x):
    a = 3
    b = 4
    fx = a * x + b
    print( fx )
en(2)

##### -- 2ø3 -- #####
print( )
print("2ø2")
# Input #
# toVal = input("Input value \n ")
# toVal = int(toVal)
toVal = 5
def to (i) :
    if i == 1:
        return 1
    else:
        return(i * to(i-1) )

toTest = to(toVal)
print (toTest)

##### -- 2ø4 -- #####
print( )
print("2ø3")
def tre1 (x, n):
    return x ** n

tre1Test = tre1(2, 4)
print (tre1Test)

##### -- 3ø0 -- #####
print( )
print("3ø0")
def fire ():
    lst = []
    lst4 = ["python"]
    lst3 = ["Hello"] * 1
    lst4 = lst4 + lst3
    lst5 = list(range(1, 4))
    return lst5

def fireF (i):
    if i == 0:
        return []
    else:
        return (fireF(i-1)) + [i]

def fireG (i):
    if i == 1:
        return [1]
    else:
        return [i] + (fireG(i-1))

fireFtest = fireF(10)
fireGTest = fireG(5)
fireTest = fire()
print(fireTest)
print(fireFtest)
print(fireGTest)

##### -- 3ø1 -- #####
print( )
print("3ø1")
def fem():
    lst = [1, 2, 3]
    result = list(map(lambda n: n / 2, lst))
    return result 

femTest = fem()
print(femTest)

#3ø2
print( )
print("3ø2")
def seks(n):
    
    return n[0]
testSeks = seks(fireFtest)
print (testSeks)

def exercise_212(A, n):
    print("Exercise 2.1-2")
    sum = 0
    for i in range(1, n):
        sum = sum + A[i]
    return sum

def exercise_213a(A,n):
    print("")
    print("Exercise 2.1-3")
    for i in range (1,n):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key
    return A

def exercise_213b(A,n):
    for i in range (1,n):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] < key:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key
    return A

# Dmfs rewrite to pseudocode
def dmfsProblem1_3a (A):
    l = len(A)
    i = 0
    failed = False
    while (i <= l):
        for j in range(i+1, l):
            if (A[i] == A[j]):
                failed = True
        i += 1
    if (failed == True):
        return "Failed"
    else:
        return "succses"

def heapify(A):
    m = len(A)
    B = list(A)
    while m > 1:
        for i in range(1, (m + 1) // 2):
            if B[2 * i - 1] >= B[2 * i]:
                B[i] = B[2 * i - 1]
            else:
                B[i] = B[2 * i]
        if m % 2 == 1:
            B[(m + 1) // 2] = B[m - 1]
        m = (m + 1) // 2
    return B

def run ():
    if (True): # Exercise 2.1-2
        lste_212 = [1, 2, 3]
        print(exercise_212(lste_212, len(lste_212)))
    if (True): # Exercise 2.1-3
        lste_213 = [5, 2, 4, 6, 1, 3]
        print("ASC : " + str(exercise_213a(lste_213, len(lste_213))))
        print("DESC: " + str(exercise_213b(lste_213, len(lste_213))))
    if (True): print(dmfsProblem1_3a([1, 2, 3, 4, 5, 6, 7]))
    if (True): print(heapify([1, 4, 5, 7, 8, 12, 2]))
run()