import bisect
def pylons(k, arr):
    n=len(arr)
    List=[]
    for i in range(n):
        if arr[i]==1:
           List.append(i) 
    end=-1
    ans=0
    istart=0
    while end<n-1:
        index=bisect.bisect_right(List,end+k,istart)-1
        if index<0:
            return -1
        istart=index
        ans+=1
        end1=List[index]+(k-1)
        if end1==end:
            return -1
        end=end1
    return ans
