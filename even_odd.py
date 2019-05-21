import itertools

myList = [1,2,3,4]

def findsubsets(S,m):
    return set(itertools.combinations(S, m))

x = findsubsets(myList, 3)
#print x


#burada sunlari ayiralim
#bir kere verdigimiz setin uzunluguna gore cift ve tek sayilari ayarlarsak
#o zaman bu fonksiyona bunlarin hepsini for loop ile verebiliriz


evenList = []
oddList = []

listLength = len(myList)
for i in range(0, listLength+1):
    x = findsubsets(myList, i)
    if( i % 2 == 0):
        evenList.append(x)
    else:
        oddList.append(x)

print "EvenList", evenList
print "OddList",  oddList
