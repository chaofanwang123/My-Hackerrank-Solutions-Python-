def connectedCell(matrix):
    def dfs(i,j):
        matrix[i][j]=2
        area=1
        for u,v in steps:
            x=i+u
            y=j+v
            if 0<=x<n and 0<=y<m and matrix[x][y]==1:
                area+=dfs(x,y)
        return area
        
    ans=0
    steps=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    n,m=len(matrix),len(matrix[0])
    for i in range(n):
        for j in range(m):
            if matrix[i][j]==1:
                ans=max(ans,dfs(i,j))
    return ans
    

matrix=[[1,1,0,0,0],[0,1,1,0,0],[0,0,1,0,1],[1,0,0,0,1],[0,1,0,1,1]]
ans=connectedCell(matrix)