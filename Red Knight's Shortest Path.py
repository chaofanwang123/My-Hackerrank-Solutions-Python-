def printShortestPath(n, i_start, j_start, i_end, j_end):
    # Print the distance along with the sequence of moves.
    end=(i_end,j_end)
    vset=set()
    vset.add((i_start,j_start))
    stack=[(i_start,j_start,'')]
    count=0
    steps=[('UL',-2,-1), ('UR',-2,1), ('R',0,2), ('LR',2,1), ('LL',2,-1), ('L',0,-2)]
    while stack:
        count+=1
        N=len(stack)
        while N>0:
            N-=1
            i,j,path=stack.pop(0)
            for direction,stepx,stepy in steps:
                x=i+stepx
                y=j+stepy
                if (x,y)==end:
                    print(count)
                    path+=' '+direction 
                    print(path[1:])
                    return
                if 0<=x<n and 0<=y<n and (x,y) not in vset:
                    vset.add((x,y))
                    stack.append((x,y,path+' '+direction))
    print('Impossible')
            
printShortestPath(6,5,1,0,5)