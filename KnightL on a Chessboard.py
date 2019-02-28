def BFS(n,i,j):
    vset=set()
    vset.add((0,0))
    dest=(n-1,n-1)
    stack=[(0,0)]
    if i!=j:
        step=[(i,j),(i,-j),(-i,j),(-i,-j),(j,i),(j,-i),(-j,i),(-j,-i)]
    else:
        step=[(i,i),(i,-i),(-i,i),(-i,-i)]
    count=0
    while stack:
        count+=1
        m=len(stack)
        while m>0:
            m-=1
            x,y=stack.pop(0)
            for stepx,stepy in step:
                x1,y1=x+stepx,y+stepy
                if (x1,y1)==dest:
                    return count
                if 0<=x1<n and 0<=y1<n and (x1,y1) not in vset:
                    vset.add((x1,y1))
                    stack.append((x1,y1))
    return -1
            
def knightlOnAChessboard(n):
    ans=[[0]*(n-1) for _ in range(n-1)]
    for i in range(n-1):
        for j in range(i,n-1):
            ans[i][j]=BFS(n,i+1,j+1)
    for i in range(n-1):
        for j in range(i+1,n-1):
            ans[j][i]=ans[i][j]
    return ans
            
ans=knightlOnAChessboard(5)
