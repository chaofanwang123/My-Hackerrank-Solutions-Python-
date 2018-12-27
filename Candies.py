def candies(n, arr):
    List=[1]*n
    i=1
    while i<n:
        if arr[i]==arr[i-1]:
            j=i+1
            while j<n and arr[j]==arr[j-1]:
                j+=1
            i=j
        elif arr[i]<arr[i-1]:
            j=i+1
            while j<n and arr[j]<arr[j-1]:
                j+=1
            for k in range(i,j-1):
                List[k]=j-k
            List[i-1]=max(List[i-1],j-i+1)
            i=j
        else:
            j=i+1
            while j<n and arr[j]>arr[j-1]:
                j+=1
            for k in range(i,j):
                List[k]=k-i+2
            i=j
    return sum(List)

n=16387
file=open('input.txt')
arr=[]
for line in file:
    arr.append(int(line))

#n=10
#arr=[2,4,2,6,1,7,8,9,2,1]
ans=candies(n,arr)