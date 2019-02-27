def steadyGene(gene):
    n=len(gene)
    lim=n//4
     
    dA,dC,dG,dT=[0]*(n+1),[0]*(n+1),[0]*(n+1),[0]*(n+1)
    for i in range(n):
        dA[i+1]=dA[i]
        dC[i+1]=dC[i]
        dG[i+1]=dG[i]
        dT[i+1]=dT[i]
        if gene[i]=='A':
            dA[i+1]+=1
        elif gene[i]=='C':
            dC[i+1]+=1
        elif gene[i]=='G':
            dG[i+1]+=1
        else:
            dT[i+1]+=1
    if dA[n]==dC[n]==dG[n]==dT[n]:
        return 0
    
    start,end=0,0
    count={}
    count['A']=dA[-1]-dA[1]+dA[0]
    count['C']=dC[-1]-dC[1]+dC[0]
    count['G']=dG[-1]-dG[1]+dG[0]
    count['T']=dT[-1]-dT[1]+dT[0]
    ans=n
    while start<=end:
        if end==n-1:
            if count[gene[start]]==lim:
                ans=min(ans,end-start+1)
                return ans
            count[gene[start]]+=1
            start+=1
            continue
        if max(count.values())>lim:
            end+=1
            count[gene[end]]-=1
            continue
        if count[gene[start]]==lim:
            ans=min(ans,end-start+1)
            end+=1
            count[gene[end]]-=1
            continue
        count[gene[start]]+=1
        start+=1
    return ans
        
gene='GAAATAAA'
ans=steadyGene(gene)
