from collections import defaultdict
def cutTheTree(data, edges):
    # Write your code here
    def dfs(i):
        vset.add(i)
        if i in map:
            return map[i]
        summ=data[i-1]
        for j in graph[i]:
            if j not in vset:
                summ+=dfs(j)
        map[i]=summ
        return summ
    graph=defaultdict(list)
    for x,y in edges:
        graph[x].append(y)
        graph[y].append(x)
    vset=set()
    total=sum(data)
    dif=total
    map={}
    dfs(1)
    for i in range(2,len(data)+1):
        dif=min(dif,abs(2*map[i]-total))
    return dif
                
#data=[100,200,100,500,100,600]
#edges=[[1,2],[2,3],[2,5],[4,5],[5,6]]
#ans=cutTheTree(data, edges)
