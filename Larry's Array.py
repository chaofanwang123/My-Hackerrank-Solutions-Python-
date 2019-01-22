def helper(B,start):
    if len(B)==2:
        return B[0]<B[1]
    index=B.index(start)
    if index%2==0:
        B.pop(index)
        return helper(B,start+1)
    else:
        B.pop(index)
        B[1],B[0]=B[0],B[1]
        return helper(B,start+1)


def larrysArray(A):
    n=len(A)
    A_final=[i for i in range(1,n+1)]
    if set(A)!=set(A_final):
        return 'NO'
    return 'YES' if helper(A,1) else 'NO'

