##### ----- Imports ----- #####


##### ----- Implementation ----- #####
''' Exercise 1: Default argument '''
def showEmployee(name, salary=9000):
    return(name, salary)

''' Exercise 2: Inner calculation '''
def innerCal(a,b):
    def inner(a_,b_):
        return a+b
    return inner(a,b) + 5

''' Exercise 3: Recusive cumulation '''
def rec(k=10):
    if k:
        return k + rec(k-1)
    else: return 0

''' Exercise 4: rename function '''
def display_student(name, age):
    print(name, age)
show_student = display_student 

''' Exercise 5: odd/even-index '''
l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]

def oddEvenIndex(a, b):
    even = []
    odd = []
    for index in range(0, len(a), 2):
        even.append(a[index])
    for index in range(1, len(b), 2):
        odd.append(a[index])
    



##### ----- Answers ----- #####
def run1():
    print('Exercise 1: Default argument')
    print(showEmployee('Ben', 12000))
    print(showEmployee('Jesse'))

    print('\nExercise 2: Inner calculaion')
    print(innerCal(5, 10))

    print('\nExercise 3: Recusive cumulation')
    print(rec())

    print('\nExercise 4: rename function')
    show_student('Emma', 26)


if (True): run1()