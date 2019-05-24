import itertools


def createCollection(a):
    new_list = []

    for m in itertools.permutations(a):
        new_list.append(m)

    newer_list = []
   
    for elm in new_list:
        elm = map(list, map(None, *elm))
        newer_list.append(elm)

    return newer_list


#provide matrix here -- by columns
matrix = []
matrix.append([0,0,0])
matrix.append([0,1,1])
matrix.append([1,0,1])
matrix.append([1,1,0])



collectionMatrix = createCollection(matrix)

for i in collectionMatrix:
    print i


