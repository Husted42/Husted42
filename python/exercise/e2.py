print("Exercise 2.1-2")
def exercise_212(A, n):
    sum = 0
    for i in range(1, n):
        sum = sum + A[i]
    return sum
lste_212 = [1, 2, 3]
print(exercise_212(lste_212, len(lste_212)))

print("")
print("Exercise 2.1-3")
def exercise_213a(A,n):
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

lste_213 = [5, 2, 4, 6, 1, 3]
print("ASC : " + str(exercise_213a(lste_213, len(lste_213))))
print("DESC: " + str(exercise_213b(lste_213, len(lste_213))))

