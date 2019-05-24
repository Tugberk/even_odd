import itertools

'''
def I(n):
    A = []
    for i in range(n):
        A.append([1 if j == i else 0 for j in range(n)])
    return A
'''

#tests:

#A = I(3)
matrix = []
matrix.append([0,0,0])
matrix.append([0,1,1])
matrix.append([1,0,1])
matrix.append([1,1,0])


#print matrix

#matrix = map(list, map(None, *matrix))




new_list = []

for m in itertools.permutations(matrix):
    #print m
    new_list.append(m)
    

for elm in new_list:
    elm = map(list, map(None, *elm))
    print elm


#bu yukaridaki kod calisiyor ama ben bunlara columnlari istedigim gibi yani gozuktugu gibi
#giremiyorum o yuzden baska turlu yapmaya calisacagim
