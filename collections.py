import itertools


matrix = []
matrix.append([0,0,0])
matrix.append([0,1,1])
matrix.append([1,0,1])
matrix.append([1,1,0])


new_list = []

for m in itertools.permutations(matrix):
    #print m
    new_list.append(m)
    

for elm in new_list:
    elm = map(list, map(None, *elm))
    print elm

