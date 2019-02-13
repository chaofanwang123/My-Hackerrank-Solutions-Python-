from collections import defaultdict
        
def lilysHomework(arr):
    d1=defaultdict(list)
    d2=defaultdict(list)
    Arr=[item for item in arr]
    n=len(arr)
    for i in range(n):
        d1[arr[i]].append(i)
        d2[arr[i]].append(i)
    arr2=sorted(arr)
    ans1=0
    for i in range(n):
        if arr[i]!=arr2[i]:
            d1[arr[i]].append(d1[arr2[i]][0])
            d1[arr[i]].pop(0)
            arr[d1[arr2[i]][0]],arr[i]=arr[i],arr[d1[arr2[i]][0]]
            d1[arr2[i]].pop(0)
            ans1+=1
    
    ans2=0
    arr2=arr2[::-1]
    for i in range(n):
        if Arr[i]!=arr2[i]:
            d2[Arr[i]].append(d2[arr2[i]][0])
            d2[Arr[i]].pop(0)
            Arr[d2[arr2[i]][0]],Arr[i]=Arr[i],Arr[d2[arr2[i]][0]]
            d2[arr2[i]].pop(0)
            ans2+=1
    return min(ans1,ans2)

arr=[3,4,2,5,1]
ans=lilysHomework(arr)