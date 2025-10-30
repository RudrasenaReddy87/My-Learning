# Next greater element 
# Given an array of integers, for each element, find the next greater element to its right.
# If there is no greater element, print -1 for that position.
# first traverse from right to left
# append to stack if stack is empty
# if stack, then check cur element >= stack top. True then pop
# if stack, add into main answer (stack top) else add -1 
# reverse the final answer

arr = [13, 7, 6, 12]
n = len(arr)
ans = []
res = []
for i in arr[n-1::-1]:
    
    while ans and i >= ans[-1]:
        ans.pop()
    
    if ans:
        res.append(ans[-1])
    else:
        res.append(-1)
    ans.append(i)

print(res[::-1])
        
    

