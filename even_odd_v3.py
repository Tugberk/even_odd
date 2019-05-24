import itertools

myList = [1, 2, 3, 4]



def findsubsets(S,m):
    return set(itertools.combinations(S, m))

evenList = []
oddList = []


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


#bu alt satir kendi hack im aslinda oddList icin cunku siralamayi itertools enteresan yapiyor
#gerci diger siralamayi da kafasina gore yapiyor burada ama cok da onemli degil gibi
#bunun calismasi icin yukarida for dongusunu 2 den baslatmak gerekiyor.
'''
evenComp.insert(0,())

for i in myList:
    oddComp.insert((i-1),(i,))
    '''




print "Even Subsets:(n=",len(evenComp),")", evenComp
print "Odd Subsets:(n=",len(oddComp),")", oddComp




#simdi S ler icin denemeler yapalim

s_white = []

for i in myList:
    for elm in evenComp:
        
        if i in elm:
            s_white.append("1")
        else:
            s_white.append("0")

print "-----------------------------------------"
print "S matrix for white pixel --> S_0"
print s_white

s_black = []

for i in myList:
    for elm in oddComp:      
        if i in elm:
            s_black.append("1")
        else:
            s_black.append("0")

print "S matrix for black pixel --> S_1"
print s_black

print "-------------------------------"
k = 2 ** (len(myList) - 1)
#k bizim matrix in n x m sinin m si


arb_list = []
matrix = []
'''
for j in range(0, k):
    arb_list.append(s_white[j])
'''


s_white_copy = []
for i in range(0, len(s_white)):
    s_white_copy.append(s_white[i])

for i in s_white_copy:
    for j in range(0,k):
        arb_list.append(s_white_copy[j])
        if(len(arb_list) == k):
            matrix.append(arb_list)
            arb_list = []
            #print matrix
            #print "White:" , s_white
            for m in range(0, k):
                if(len(s_white_copy) == 1):
                    print ""
                else:
                    s_white_copy.pop(0)
        
                    

matrix.append(arb_list)
arb_list = []





matrix_black = []
s_black_copy = []
for i in range(0, len(s_black)):
    s_black_copy.append(s_black[i])



print "------------------"
for i in s_black_copy:
    for j in range(0,k):
        arb_list.append(s_black_copy[j])
        if(len(arb_list) == k):
            matrix_black.append(arb_list)
            arb_list = []
            print matrix_black
            print s_black_copy
            for m in range(0, k):
                if(len(s_black_copy) == 1):
                    print ""
                else:
                    s_black_copy.pop(0)
                    print s_black_copy, "popped"


print "White S Matrix"
print "-----------------"
matrix.remove([])
for i in matrix:
    print i
    


print "Black S Matrix"
print "-----------------"
#black_s_matrix.remove([])
for i in matrix_black:
    print i
