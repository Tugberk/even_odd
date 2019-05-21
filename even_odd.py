import itertools

myList = [1,2,3,4]

def findsubsets(S,m):
    return set(itertools.combinations(S, m))

evenList = []
oddList = []

listLength = len(myList)
for i in range(0, listLength+1):
    x = findsubsets(myList, i)
    if( i % 2 == 0):
        evenList.append(x)
    else:
        oddList.append(x)

'''print "EvenList", evenList
print "OddList",  oddList
'''

print "Even List"
for elm in evenList:
    print elm
print "Odd List"
for elm in oddList:
    print elm
