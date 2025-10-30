'''
Stack : Stack is a linear data structure, follows the principle of (LIFO).
- LIFO : last in first out also called FILO {First in last out}.
- The last element inserted inside the stack is removed first.

operations: 
- Empty stack 
- Push
- Pop
- Full
- Peek

1. The pointer called "TOP" is used to keep track of the top element in stack.
2. when we initializing the stack, we set its value to -1 (for check stack is empty or not)
3. if element inserted then increase the top += 1
4. if element remove then decrease the top -= 1
5. Before pushing we check stack is full or not.(overflow)
6. Before popping we check stack is empty or not.(underflow)
O(1)
'''
def h():
    print( "---------------------------------------------------------------------------------------")
# Stack implementation using list

stack = [] # stack initialization
stack.append(10) # stack push
stack.append(20) # stack push
print(stack) # print stack
print(stack.pop()) # stack pop
print(stack) # print stack after pop
print(stack[-1]) # stack peek
print(len(stack) == 0) # check stack is empty

h()
# Stack using array

class Array_stack:
    def __init__(self, cap):
        # capacity for array to store stack elements
        self.arr = [0] * cap
        self.top = -1
        self.cap = cap
    
    def isempty(self):
        return self.top == -1
    
    def isfull(self):
        return self.cap - 1 == self.top
    
    def peek(self):
        if self.top == -1:
            print("Stack is empty")
        return self.arr[self.top]
    
    def push(self,val):
        if self.top == self.cap-1:
            print("Stack Overflow")
            return 
        self.top += 1
        self.arr[self.top] = val
        
    def pop(self):
        if self.top == -1:
            print("Stack underflow")
            return 
        
        val = self.arr[self.top]
        self.top -= 1
        return val
    

arr_stack = Array_stack(8) # arr capacity '8'
print(arr_stack.isempty()) # True
arr_stack.push(10) # push into the stack
arr_stack.push(20)
arr_stack.push(60)
arr_stack.push(40)
arr_stack.push(80)

print(arr_stack.peek()) # last element ex. '80'

arr_stack.pop()
arr_stack.pop()
print(arr_stack.peek()) # last element ex. '60'
arr_stack.push(60)
arr_stack.push(40)
arr_stack.push(80)
arr_stack.push(60)
arr_stack.push(60)
arr_stack.push(60) # if we push it will return stack overflow (exceed the arr size)
arr_stack.pop()
arr_stack.pop()
arr_stack.pop()
arr_stack.pop()
arr_stack.pop()
arr_stack.pop()
arr_stack.pop()
arr_stack.pop()
arr_stack.pop() # stack underflow
h()

