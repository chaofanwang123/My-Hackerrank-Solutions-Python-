# Complete the evenForest function below.
from collections import defaultdict
def evenForest(t_nodes, t_edges, t_from, t_to):
    def dfs(u,parent_node):
        ans=1
        for v in d[u]:
            if v!=parent_node:
                ans+=dfs(v,u)
        count[u-1]=ans
        return ans
    def helper(u,parent_node):
        ans=0
        for v in d[u]:
            if v!=parent_node:
                if count[v-1]%2==0:
                    ans+=1
                ans+=helper(v,u)
        return ans

    count=[1]*t_nodes
    d=defaultdict(list)
    for i in range(len(t_from)):
        d[t_from[i]].append(t_to[i])
        d[t_to[i]].append(t_from[i])
    root=1
    dfs(root,None)
    return helper(root,None)
