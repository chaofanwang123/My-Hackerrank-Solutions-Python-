# Complete the prims function below.
def prims(n, edges, start):
    def find_min_dist(dist,visited):
        mind=float('inf')
        ans=None
        for i in range(n):
            if not visited[i] and dist[i]<mind:
                mind=dist[i]
                ans=i
        return (ans,mind)
    
    dist=[float('inf')]*n
    dist[start-1]=0
    visited=[0]*n
    d={}
    for u,v,w in edges:
        d[(u-1,v-1)]=w
        d[(v-1,u-1)]=w
    ans=0
    for _ in range(n):
        u,mind=find_min_dist(dist,visited)
        ans+=mind
        visited[u]=1
        # update min dist after adding u
        for i in range(n):
            if not visited[i] and (u,i) in d and dist[i]>d[(u,i)]:
                dist[i]=d[(u,i)]
    return ans
