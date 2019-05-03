# Complete the organizingContainers function below.
from collections import Counter
def organizingContainers(container):
    list1=[sum(row) for row in container]
    list2=[0]*len(container[0])
    for j in range(len(container[0])):
        for i in range(len(container)):
            list2[j]+=container[i][j]
    return 'Possible' if Counter(list1)==Counter(list2) else 'Impossible'
