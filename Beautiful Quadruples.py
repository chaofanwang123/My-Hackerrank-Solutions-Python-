import bisect
from collections import defaultdict
def beautifulQuadruples(a, b, c, d):
    a,b,c,d=sorted([a,b,c,d])
    total=0
    for i in range(1,a+1):
        for j in range(i,b+1):
            total+=(d+1-j+d+1-c)*(c+1-j)//2
    D=defaultdict(list)
    for i in range(1,a+1):
        for j in range(i,b+1):
            temp=i^j
            bisect.insort(D[temp],j)
    count=0
    for i in range(1,c+1):
        for j in range(i,d+1):
            temp=i^j
            if temp in D and i>=D[temp][0]:
                index=bisect.bisect_right(D[temp],i)
                count+=index
    return total-count
