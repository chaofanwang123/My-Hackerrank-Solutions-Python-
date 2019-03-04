import bisect
def minimumLoss(price):
    ans=float('inf')
    stack=[price[0]]
    for num in price[1:]:
        if num<stack[0]:
            ans=min(ans,stack[0]-num)
            stack.insert(0,num)
        else:
            index=bisect.bisect(stack,num)
            if index<len(stack):
                ans=min(ans,stack[index]-num)
            stack.insert(index,num)
    return ans

price=[20,7,8,2,5]
ans=minimumLoss(price)