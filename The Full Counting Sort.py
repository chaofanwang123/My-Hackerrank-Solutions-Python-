def countSort(arr):
    n=len(arr)
    if n==1:
        print(arr[0][1])
    d={}
    key=[]
    for i in range(n//2):
        arr[i][1]='-'
    for i in range(n):
        if arr[i][0] in d:
            d[arr[i][0]]+=' '+arr[i][1]
        else:
            d[arr[i][0]]=arr[i][1]
            key.append(arr[i][0])
    key.sort()
    ans=''
    for item in key:
        ans+=' '+d[item]
    print(ans[1:])
