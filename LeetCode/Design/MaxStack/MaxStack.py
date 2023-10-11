# Design a max stack data structure that supports the stack operations and supports finding the stack's maximum element.

# Implement the MaxStack class:

    # MaxStack() Initializes the stack object.
    # void push(int x) Pushes element x onto the stack.
    # int pop() Removes the element on top of the stack and returns it.
    # int top() Gets the element on the top of the stack without removing it.
    # int peekMax() Retrieves the maximum element in the stack without removing it.
    # int popMax() Retrieves the maximum element in the stack and removes it. If there is more than one maximum element, only
    # remove the top-most one.

# You must come up with a solution that supports O(1) for each top call and O(logn) for each other call.


from RBT import RedBlackTree

class MaxStack:

    def __init__(self):
        self.stack = RedBlackTree()
        self.values = RedBlackTree()
        self.idx = 0

    def push(self, x):
        self.stack.insert((self.idx, x))
        self.values.insert((x, self.idx))
        self.idx += 1

    def pop(self):
        idx, val = self.stack.pop()
        self.values.delete((val, idx))
        return val
    
    def top(self):
        node = self.stack.top()
        return node.val[1]

    def peekMax(self):
        node = self.values.top()
        return node.val[0]
    
    def popMax(self):
        val, idx = self.values.pop()
        self.stack.delete((idx, val))
        return val
    
stack = MaxStack()

stack.push(5)
stack.push(1)
stack.push(5)
print(stack.top())
print(stack.popMax())
print(stack.top())
print(stack.peekMax())
print(stack.pop())
print(stack.top())