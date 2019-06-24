def min_oper(n,m):
    # min# of operation to reduce n to m
    if n==m:
        return 0
    oper1,rem=(n-m)//5,(n-m)%5
    oper2=0
    if rem==1 or rem==2:
        oper2=1
    elif rem==3 or rem==4:
        oper2=2
    return oper1+oper2
def equal(arr):
    arr.sort()
    dp=[[0]*5 for _ in range(len(arr))]
    # dp[k][n] is the min# of subtraction operation (-1,2, or -5 on only one item) to get the first k items to arr[0]-n
    for j in range(5):
        dp[0][j]=min_oper(arr[0],arr[0]-j)
    for i in range(1,len(arr)):
        for j in range(5):
            dp[i][j]=min_oper(arr[i],arr[0]-j)+dp[i-1][j]
    return min(dp[-1][j] for j in range(5))

