class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
def helper(root):
    if root:
        minv,maxv=root.data,root.data
        if root.left:
            minl,maxl,Bol_l=helper(root.left)
            if not Bol_l or maxl>=root.data:
                return (0,0,False)
            minv=min(minv,minl)
        if root.right:
            minr,maxr,Bol_r=helper(root.right)
            if not Bol_r or minr<=root.data:
                return (0,0,False)
            maxv=max(maxv,maxr)
        return (minv,maxv,True)

def checkBST(root):
    if not root:
        return 'Yes'
    minv,maxv,Bol=helper(root)
    return Bol

def inorder(root,List):
    if root:
        inorder(root.left,List)
        List.append(root.data)
        inorder(root.right,List)
        
def checkBST2(root):
    if not root:
        return 'Yes'
    List=[]
    inorder(root,List)
    for i in range(len(List)-1):
        if List[i]>=List[i+1]:
            return 'No'
    return 'Yes'

root=node(3)
root.left=node(2)
root.left.left=node(1)
root.left.right=node(4)
root.right=node(6)
root.right.left=node(5)
root.right.right=node(7)

ans=checkBST2(root)