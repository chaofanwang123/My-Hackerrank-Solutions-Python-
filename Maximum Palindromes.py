from collections import Counter
def com(x,y):
    ans=1
    for i in range(y):
        ans*=x-i
    for i in range(y):
        ans//=i+1
    return ans
    
def answerQuery(l, r, s):
    s1=s[l-1:r]
    n=len(s1)
    if n==1:
        return 1
    maxl=0
    d=Counter(s1)
    note=0
    for item in d:
        if d[item]%2:
            note+=1
        maxl+=d[item]//2*2
    if note!=0:
        maxl+=1
    if maxl%2:
        N=maxl//2
        ans=note
        for item in d:
            if d[item]>1:
                m=d[item]//2
                ans*=com(N,m)
                N-=m
                ans%=(10**9+7)
    else:
        N=maxl//2
        ans=1
        for item in d:
            if d[item]>1:
                m=d[item]//2
                ans*=com(N,m)
                N-=m
                ans%=(10**9+7)
    return ans
    
ans=answerQuery(1, 4, 'week')

