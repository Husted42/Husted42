lst1 = [15, 4, 6, 7, 8, 6]
lst2 = [5, 4, 3, 2, 1]

def insertionSort(A, n):
    for i in range (1, n):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j+1] = A[j]
            j = j - 1
        A[j+1] = key
    return A

def sumArray(A, n):
    sum = 0
    for i in range (0, n):
        sum = sum + A[i]
    return sum

def run():
    print("Insertion sort")
    print("Before: " + str(lst2))
    print("After:  " + str(insertionSort(lst2, len(lst2))))

    print("\nSum of array upto n")
    print("sum of lst2: " + str(sumArray(lst2, len(lst2))))
run()
