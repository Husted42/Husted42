##### -- phonetic alphabet -- #####
#Alfa, Bravo, Charlie, Delta, Echo, Foxtrot

##### -- variables -- #####
lst1 = ['Alpha', 'Bravo', 'Charlie']
lst2 = ['Alpha', 'Delta']

##### -- Exercises -- #####
#Exercise 0
def notIn(l1, l2):
    lst = []
    for elm in l1:
        if elm not in l2:
            lst.append(elm)
    return lst

if 0 :
        print('elements in list 1 not in list 2')
        print(notIn(lst1, lst2))
        print(set(lst1) - set(lst2), '\n')

#Exercise 1
''' 54 % 24 == 6, 24 % 6 == 0 '''
def gdc(a, b):
    if b == 0:
        return a
    else:
        return gdc(b, (a % b))

if 0 :
        print('Greatest common divisor')
        print(gdc(54, 24), '\n')

''' https://www.w3resource.com/python-exercises/puzzles/index.php (06/06/2023)'''
#Ecercise 2
def twoNineteen (lst):
    a_, b_ = 0, 0
    for i in range (0, len(lst)):
          if lst[i] == 19: a_ = a_ + 1
          if lst[i] == 5: b_ = b_ + 1 
    return (a_ == 2 and b_ >= 3)

if 0 :
     print('3 x 19 == True, n x 5 where n >= 3 == True ')
     print(twoNineteen([19, 19, 15, 5, 3, 5, 5, 2])) #True
     print(twoNineteen([19, 15, 15, 5, 3, 3, 5, 2])) #False
     print(twoNineteen([19, 19, 5, 5, 5, 5, 5]), '\n') #True
     
#Ecercise 3
def fithThrice(lst):
     a_ = 0
     for i in range (0, len(lst)):
          if lst[i] == lst[4]: a_ = a_ + 1
     return (len(lst) == 8 and a_ == 3)

if 1 :
    print('Accepts a list of integers and calculates the length and the fifth element. \nReturn true if the length of the list is 8 and the fifth element occurs thrice in the said list')
    print(fithThrice([19, 19, 15, 5, 5, 5, 1, 2])) #True
    print(fithThrice([19, 15, 5, 7, 5, 5, 2])) #False
    print(fithThrice([11, 12, 14, 13, 14, 13, 15, 14])) #True
    print(fithThrice([19, 15, 11, 7, 5, 6, 2])) #False