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
    if (False): # Exercise 2.1-2
        lste_212 = [1, 2, 3]
        print(exercise_212(lste_212, len(lste_212)))
    if (False): # Exercise 2.1-3
        lste_213 = [5, 2, 4, 6, 1, 3]
        print("ASC : " + str(exercise_213a(lste_213, len(lste_213))))
        print("DESC: " + str(exercise_213b(lste_213, len(lste_213))))
    if (True): print(dmfsProblem1_3a([1, 2, 3, 4, 5, 6, 7]))
    if (True): print(heapify([1, 4, 5, 7, 8, 12, 2]))
run()