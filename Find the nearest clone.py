from collections import defaultdict
def findShortest(graph_nodes, graph_from, graph_to, ids, val):
    # solve here
    d=defaultdict(list)
    vset=defaultdict(set)
    for i in range(len(graph_from)):
        d[graph_from[i]].append(graph_to[i])
        d[graph_to[i]].append(graph_from[i])
    stack=[]
    for i in range(1,graph_nodes+1):
        if ids[i-1]==val:
            stack.append((i,i))
            vset[i].add(i)
    count=0
    while stack:
        count+=1
        n=len(stack)
        temp_set=dict()
        while n>0:
            n-=1
            u,origin=stack.pop(0)
            for v in d[u]:
                if v in vset:
                    if origin not in vset[v]:
                        return 2*count-1
                elif v not in temp_set:
                    temp_set[v]=origin
                else:
                    if temp_set[v]!=origin:
                        return 2*count
        for point,origin in temp_set.items():
            vset[point].add(origin)
            stack.append((point,origin))
    return -1
        
graph_nodes=4
graph_from=[1,1,4]
graph_to=[2,3,2]
ids=[1,2,3,4]
val=1
ans=findShortest(graph_nodes, graph_from, graph_to, ids, val)           
        

