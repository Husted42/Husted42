def findRight(lst, tgt):
    result = []
    def helper(lst, tgt, comb, result):
        if tgt == 0:
            result.append(comb)
        elif tgt < 0:
            return
        else:
            for i in range(len(lst)):
                helper(lst[i+1:], tgt-lst[i], comb+[lst[i]], result)
    helper(lst, tgt, [], result)
    return result

def JacobsFrog(n):
    lst = []
    for i in range (1, n+1):
        lst.append(i)
    if sum(lst) % 2 != 0:
        print("Not possible")
        return None
    right = (findRight(lst, (sum(lst)/2)))[0]
    for i in lst:
        if (lst[i-1] in right):
            lst[i-1] = True
        else:
            lst[i-1] = False
    for j in range(1, len(lst)+1):
        if lst[j-1] == True:
            print("jump lenght " + str(j) + " right ")
        else:
            print("jump lenght " + str(j) + " left ")
            
print("Kontrol for n = 3")
JacobsFrog(3)
print("")
print("Kontrol for n = 4")
JacobsFrog(4)
print("")
print("Kontrol for n = 6")
JacobsFrog(6)
print("")
print("Kontrol for n = 7")
JacobsFrog(7)
print("")
print("Kontrol for n = 8")
JacobsFrog(8)
print("")
