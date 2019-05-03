# Complete the quickestWayUp function below.
def quickestWayUp(ladders, snakes):
    d1,d2={},{}
    for x,y in ladders:
        d1[x]=y
    for x,y in snakes:
        d2[x]=y
    stack=[1]
    dest=100
    vset=set()
    vset.add(1)
    count=0
    while stack:
        count+=1
        N=len(stack)
        while N>0:
            N-=1
            x=stack.pop(0)
            for i in range(1,7):
                x1=x+i
                if x1 in d1:
                    x1=d1[x1]
                if x1 in d2:
                    x1=d2[x1] 
                if x1>=dest:
                    return count
                if x1 not in vset:
                    vset.add(x1)
                    stack.append(x1)
    return -1
