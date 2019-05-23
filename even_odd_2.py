import itertools

myList = [1, 2, 3, 4]

def findsubsets(S,m):
    return set(itertools.combinations(S, m))

evenList = []
oddList = []

print findsubsets(myList, 1)


#1 eleman dedigimizde bi bug var.
#0. elemani kendimiz ekleyebiliriz, ustune de 1 i kendimiz tek tek ekleyebiliriz
#bir bunu deneyelim oyle olusturalim


listLength = len(myList)
for i in range(0, listLength+1):
    x = findsubsets(myList, i)
    if( i % 2 == 0):
        evenList.append(x)
    else:
        oddList.append(x)

print "----"

evenComp = []
oddComp = []

for set in evenList:
    for i in set:
        evenComp.append(i)

for set in oddList:
    for i in set:
        oddComp.append(i)

print "Even Subsets:(",len(evenComp),")", evenComp
print "Odd Subsets:(",len(oddComp),")", oddComp


#simdi S ler icin denemeler yapalim

s_white = []

for i in myList:
    for elm in evenComp:
        
        if i in elm:
            s_white.append("1")
        else:
            s_white.append("0")

print "-----------------------------------------"
print "S matrix for white pixel"
print s_white

s_black = []

for i in myList:
    for elm in evenComp:
        
        if i in elm:
            s_black.append("1")
        else:
            s_black.append("0")

print "S matrix for black pixel"
print s_black






