def almostSorted(arr):
    index1,index2=None,None
    i=0
    n=len(arr)
    while i<len(arr)-1:
        if arr[i]>arr[i+1]:
            if index1==None:
                index1=i
            elif index2==None:
                if i-1==index1:
                    j=i+1
                    while j<n-1 and arr[j]>=arr[j+1]:
                        j+=1
                    if (index1==0 or arr[index1-1]<=arr[j]) and arr[index1]<=arr[j+1]:
                        for k in range(j+1,n-1):
                            if arr[k]>arr[k+1]:
                                print('no')
                                return
                        print('yes'+'\nreverse '+str(index1+1)+' '+str(j+1))
                        return
                    print('no')
                    return
                else:
                    if (index1==0 or arr[index1-1]<=arr[i]<=arr[index1+1]) and (arr[i-1]<=arr[index1]<=arr[i+1]):
                        j=i+1
                        for j in range(i+1,n-1):
                            if arr[j]>arr[j+1]:
                                print('no')
                                return
                        print('yes'+'\nswap '+str(index1+1)+' '+str(i+1))
                        return
                    elif (index1==0 or arr[index1-1]<=arr[i+1]<=arr[index1+1]) and (i+2==n or arr[i]<=arr[index1]<=arr[i+2]):
                        j=i+1
                        for j in range(i+1,n-1):
                            if arr[j]>arr[j+1]:
                                print('no')
                                return
                        print('yes'+'\nswap '+str(index1+1)+' '+str(i+2))
                        return
                    print('no')
                    return
        i+=1
    if index1==None:
        print('yes')
        return
    if index2==None:
        if index1==len(arr)-2 or (index1==0 and arr[index1]<=arr[index1+2]):
            print('yes'+'\nswap '+str(index1+1)+' '+str(index1+2))
            return
        if index1==0:
            if arr[index1]<=arr[index1+2]:
                print('yes'+'\nswap '+str(index1+1)+' '+str(index1+2))
                return
            print('no')
            return
        if arr[index1-1]<=arr[index1+1] and arr[index1]<=arr[index1+2]:
            print('yes'+'\nswap '+str(index1+1)+' '+str(index1+2))
            return
        print('no')
        return
    


