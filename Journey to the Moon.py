from collections import defaultdict
def journeyToMoon(n, astronaut):
    def dfs(i):
        vset.add(i)
        count=1
        if i in d:
            for j in d[i]:
                if j not in vset:
                    count+=dfs(j)
        return count
    d=defaultdict(list)
    for i,j in astronaut:
        d[i].append(j)
        d[j].append(i)
    country=[]
    vset=set()
    for i in range(n):
        if i not in vset:
            country.append(dfs(i))
    ans=0
    for i in range(len(country)):
        ans+=country[i]*(n-country[i])
    return ans//2
