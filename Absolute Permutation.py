def absolutePermutation(n, k):
    if k==0:
        return [i for i in range(1,n+1)]
    if n%(2*k)!=0:
        return [-1]
    m=n//(2*k)
    ans=[]
    for i in range(m):
        ans+=[i*2*k+k+1+j for j in range(k)]+[i*2*k+1+j for j in range(k)]
    return ans

k=1
n=2
ans=absolutePermutation(n, k)

