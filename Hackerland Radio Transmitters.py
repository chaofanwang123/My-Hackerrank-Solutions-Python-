import bisect
def hackerlandRadioTransmitters(x, k):
    # first divide x into clusters where each cluster has any two adjacent distance<=k
    chunk=[]
    x.sort()
    temp=[x[0]]
    for i in range(len(x)-1):
        if x[i+1]-x[i]<=k:
            temp.append(x[i+1])
        else:
            chunk.append(temp)
            temp=[x[i+1]]
    chunk.append(temp)
    ans=0
    for segment in chunk:
        while segment:
            index=bisect.bisect_right(segment,segment[0]+k,0)-1
            index2=bisect.bisect_right(segment,segment[index]+k,index+1)
            segment=segment[index2:]
            ans+=1
    return ans
x=[1,2,3,5,9]
k=1
ans=hackerlandRadioTransmitters(x, k)
            
            

