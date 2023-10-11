# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# Implement the MinStack class:

    # MinStack() initializes the stack object.
    # void push(int val) pushes the element val onto the stack.
    # void pop() removes the element on the top of the stack.
    # int top() gets the top element of the stack.
    # int getMin() retrieves the minimum element in the stack.

# You must implement a solution with O(1) time complexity for each function.

class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val):
        if not self.stack:
            self.stack.append([val, val])
        else:
            currMin = self.stack[-1][1]
            self.stack.append([val, min(val, currMin)])
    
    def pop(self):
        self.stack.pop()
    
    def top(self):
        return self.stack[-1][0]
    
    def getMin(self):
        return self.stack[-1][1]
    
stack = MinStack()
stack.push(-2)
stack.push(0)
stack.push(-3)

print(stack.getMin())
stack.pop()
print(stack.top())
print(stack.getMin())