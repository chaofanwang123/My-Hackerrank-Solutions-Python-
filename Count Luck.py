def countLuck(matrix, k):
    def dfs(i,j):
        if (i,j)==des:
            return True
        vset.add((i,j))
        if i+1<n and matrix[i+1][j]!='X' and (i+1,j) not in vset and dfs(i+1,j):
            return True
        if i-1>=0 and matrix[i-1][j]!='X' and (i-1,j) not in vset and dfs(i-1,j):
            return True
        if j+1<m and matrix[i][j+1]!='X' and (i,j+1) not in vset and dfs(i,j+1):
            return True
        if j-1>=0 and matrix[i][j-1]!='X' and (i,j-1) not in vset and dfs(i,j-1):
            return True
        vset.remove((i,j))
        return False
    n,m=len(matrix),len(matrix[0])
    for i in range(n):
        for j in range(m):
            if matrix[i][j]=='M':
                start=(i,j)
            if matrix[i][j]=='*':
                des=(i,j)
    vset=set()
    dfs(start[0],start[1])
    count=0
    directions=[(1,0),(-1,0),(0,1),(0,-1)]
    for x,y in vset:
        for stepx,stepy in directions:
            if 0<=x+stepx<n and 0<=y+stepy<m and (x+stepx,y+stepy) not in vset and matrix[x+stepx][y+stepy]=='.':
                count+=1
                break
    return 'Impressed' if count==k else 'Oops!'

matrix=['XXXXXXXXXXXXXXXXX',
'XXX.XX.XXXXXXXXXX',
'XX.*..M.XXXXXXXXX',
'XXX.XX.XXXXXXXXXX',
'XXXXXXXXXXXXXXXXX']
k=1
ans=countLuck(matrix, k)