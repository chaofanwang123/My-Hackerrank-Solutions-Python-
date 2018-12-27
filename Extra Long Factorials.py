def mul(s1,s2):
    m,n=len(s1),len(s2)
    s1=s1[::-1]
    s2=s2[::-1]
    res=[0]*(m+n)
    add=0
    for i in range(m+n):
        res[i]=add
        for j in range(max(0,i+1-n),min(i,m-1)+1):
            res[i]+=s1[j]*s2[i-j]
        add=res[i]//10
        res[i]=res[i]%10
    if add>0:
        res.append(1)
    return res[::-1]
def extraLongFactorials(n):
    if n==1:
        return 1
    cur=[1]
    for i in range(2,n+1):
        num=[int(item) for item in list(str(i))]
        cur=mul(cur,num)
    cur=''.join(str(item) for item in cur)
    return int(cur)

ans=extraLongFactorials(25)