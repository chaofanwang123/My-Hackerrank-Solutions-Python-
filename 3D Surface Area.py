def surfaceArea(A):
    H,W=len(A),len(A[0])
    area=0
    for i in range(H):
        area+=2*W+4*sum(A[i])
    for i in range(H-1):
        overlap=0
        for j in range(W):
            overlap+=min(A[i][j],A[i+1][j])
        area-=overlap*2
    for j in range(W-1):
        overlap=0
        for i in range(H):
            overlap+=min(A[i][j],A[i][j+1])
        area-=overlap*2
    return area

A=[[1,3,4],[2,2,3],[1,2,4]]
ans=surfaceArea(A)