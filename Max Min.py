def maxMin(k, arr):
    n=len(arr)
    arr.sort()
    ans=arr[k-1]-arr[0]
    for i in range(1,n-k+1):
        ans=min(ans,arr[k-1+i]-arr[i])
    return ans

k=5
arr=[4504,1520,5857,4094,4157,3902,822,6643,2422,7288,8245,9948,2822,1784,7802,3142,9739,5629,5413,7232]
ans=maxMin(k, arr)
