# Complete the bfs function below.
from collections import defaultdict
def bfs(n, m, edges, s):
    d=defaultdict(list)
    for u,v in edges:
        d[u].append(v)
        d[v].append(u)
    dist=[-1]*n
    dist[s-1]=0
    stack=[s]
    while stack:
        N=len(stack)
        while N>0:
            N-=1
            u=stack.pop(0)
            if u in d:
                for v in d[u]:
                    if dist[v-1]==-1:
                        dist[v-1]=dist[u-1]+6
                        stack.append(v)
    del dist[s-1]
    return dist
