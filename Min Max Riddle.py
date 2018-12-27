def riddle(arr):
    # complete this function
    n=len(arr)
    ans=[max(arr)]
    dp=arr
    for i in range(1,n):
        m=len(dp)-1
        tmp=[[]]*m
        for j in range(m):
            tmp[j]=min(dp[j],dp[j+1])
        ans.append(max(tmp))
        dp=tmp
    return ans

arr=[2,6,1,12]
ans=riddle(arr)

