# Complete the minimumBribes function below.
def minimumBribes(q):
    count=0
    n=len(q)
    if n==1:
        return 0
    for i in range(n-1,1,-1):
        if q[i]!=i+1:
            if q[i-1]==i+1:
                count+=1
                q[i-1],q[i]=q[i],q[i-1]
            elif q[i-2]==i+1:
                count+=2
                q[i-2],q[i-1],q[i]=q[i-1],q[i],q[i-2]
            else:
                return 'Too chaotic'      
    if q[1]!=2:
        count+=1
    return count
