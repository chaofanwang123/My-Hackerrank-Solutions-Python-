from collections import Counter
def nonDivisibleSubset(k, S):
    if k==1 or len(S)==1:
        return 1
    S=[item%k for item in S]
    d=Counter(S)
    ans1,ans2=0,0
    if 0 in d or k in d:
        ans1+=1
    if 0 in d:
        del d[0]
    if k in d:
        del d[k]
    if k%2==0 and k//2 in d:
        ans1+=1
        del d[k//2]
    for num in d:
        if k-num not in d:
            ans1+=d[num]
        else:
            ans2+=max(d[num],d[k-num])
            
    return ans1+ans2//2

k=4
S=[1,2,3,4,5,6,7,8,9,10]
ans=nonDivisibleSubset(k, S)

