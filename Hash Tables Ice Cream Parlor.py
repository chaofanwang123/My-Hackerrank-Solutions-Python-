from collections import defaultdict
def whatFlavors(cost, money):
    d=defaultdict(list)
    n=len(cost)
    for i in range(n):
        d[cost[i]].append(i+1)
    for i in range(n):
        temp=money-cost[i]
        if temp in d:
            if temp!=cost[i]:
                print(i+1,d[temp][0])
                return
            elif len(d[temp])>=2:
                print(i+1,d[temp][1])
                return

cost=[1,4,5,3,2]
money=4
ans=whatFlavors(cost, money)
