from collections import defaultdict
def freqQuery(queries):
    d=defaultdict(int)
    d2=defaultdict(int)
    ans=[]
    for x,y in queries:
        if x==1:
            d[y]+=1
            d2[d[y]]+=1
        elif x==2:
            if y in d and d[y]>0:
                d2[d[y]]-=1
                d[y]-=1
                d2[d[y]]+=1
        else:
            if y in d2 and d2[y]>0:
                ans.append(1)
            else:
                ans.append(0)
    return ans

if __name__ == '__main__':
    fptr = open('D:\\Hackerrank\\input.txt', 'r')
    q = fptr.read()
    p=q.split()[1:]
    queries = []

    for i in range(len(p)//2):
        queries.append([int(p[2*i]),int(p[2*i+1])])

    ans = freqQuery(queries)
    fptr2 = open('D:\\Hackerrank\\output.txt', 'r')
    q = fptr.read()
    p=q.split()
    ans2=[int(item) for item in p]