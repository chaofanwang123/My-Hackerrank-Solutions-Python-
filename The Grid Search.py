def gridSearch(G, P):
    R,C=len(G),len(G[0])
    r,c=len(P),len(P[0])
    for i in range(R):
        start_index=G[i].find(P[0])
        if start_index!=-1:
            while start_index!=-1:
                ii=1
                while ii<r and G[i+ii][start_index:start_index+c]==P[ii]:
                    ii+=1
                if ii==r:
                    return 'YES'
                start_index=G[i].find(P[0],start_index+1)
    return 'NO'

G=['7283455864',
'6731158619',
'8988242643',
'3830589324',
'2229505813',
'5633845374',
'6473530293',
'7053106601',
'0834282956',
'4607924137']
P=['9505',
'3845',
'3530']
ans=gridSearch(G,P)