import bisect
def gridlandMetro(n, m, k, track):
    d={}
    for row, col1, col2 in track:
        if row not in d:
            d[row]=[col1, col2]
        else:
            index1=bisect.bisect_left(d[row],col1)
            index2=bisect.bisect_right(d[row],col2)
            if index1%2:
                if index2%2:
                    d[row][index1:index2]=[]
                else:
                    d[row][index1:index2]=[col2]
            else:
                if index2%2:
                    d[row][index1:index2]=[col1]
                elif index1!=index2:
                    d[row][index1:index2]=[col1,col2]
                else:
                    d[row].insert(index1,col1)
                    d[row].insert(index1+1,col2)
    area=0
    for row in d.values():
        for i in range(len(row)//2):
            area+=row[2*i+1]-row[2*i]+1
    return m*n-area
        
n,m,k=1,5,3
track=[[1,1,2],[1,2,4],[1,3,5]]
ans=gridlandMetro(n, m, k, track)
