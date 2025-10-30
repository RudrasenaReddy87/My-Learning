# Next small element using stack
# Given an array of integers, for each element, find the next smaller element to its right.
# If no smaller element exists, print -1 for that element.

# same login as next greater element
arr = [13, 7, 6, 12]
res = []
stack = []
for i in arr[len(arr) - 1::-1]:
    
    while stack and stack[-1] >= i:
        stack.pop()
        
    res.append(stack[-1] if stack else -1)
    stack.append(i)
    
print(res[::-1])