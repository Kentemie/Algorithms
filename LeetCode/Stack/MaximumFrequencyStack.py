# Design a stack-like data structure to push elements to the stack and pop the most frequent element from the stack.

# Implement the FreqStack class:

    # FreqStack() constructs an empty frequency stack.
    # void push(int val) pushes an integer val onto the top of the stack.
    # int pop() removes and returns the most frequent element in the stack.
        # If there is a tie for the most frequent element, the element closest to the stack's top is removed and returned.

class FreqStack:
    def __init__(self):
        self.frequency = {}
        self.stack = {}
        self.maxFreq = 0

    def push(self, val):
        self.frequency[val] = self.frequency.get(val, 0) + 1
        valueFreq = self.frequency[val]

        if valueFreq > self.maxFreq:
            self.maxFreq = valueFreq
            self.stack[valueFreq] = []

        self.stack[valueFreq].append(val)
        
    def pop(self):
        res = self.stack[self.maxFreq].pop()
        self.frequency[res] -= 1

        if not self.stack[self.maxFreq]:
            self.maxFreq -= 1

        return res
    
freqStack = FreqStack()
freqStack.push(5)
freqStack.push(7)
freqStack.push(5)
freqStack.push(7)
freqStack.push(4)
freqStack.push(5)

print(freqStack.stack)

print(freqStack.pop())
print(freqStack.pop())
print(freqStack.pop())
print(freqStack.pop())