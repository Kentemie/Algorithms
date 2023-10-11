# Queue

# from threading import Lock
# class MyCircularQueue:

#     def __init__(self, k: int):
#         self.queue = [0] * k
#         self.head = 0
#         self.count = 0
#         self.capacity = k
#         self.queueLock = Lock()

#     def enQueue(self, value: int) -> bool:
#         with self.queueLock:
#             if self.isFull():
#                 return False
#             self.queue[(self.head + self.count) % self.capacity] = value
#             self.count += 1
#         return True
        
#     def deQueue(self) -> bool:
#         if self.isEmpty():
#             return False
#         self.head = (self.head + 1) % self.capacity
#         self.count -= 1
#         return True

#     def Front(self) -> int:
#         if self.isEmpty():
#             return -1
#         return self.queue[self.head]

#     def Rear(self) -> int:
#         if self.isEmpty():
#             return -1
#         return self.queue[(self.head + self.count - 1) % self.capacity]

#     def isEmpty(self) -> bool:
#         return self.count == 0

#     def isFull(self) -> bool:
#         return self.count == self.capacity
    
# obj = MyCircularQueue(5)
# param_1 = obj.enQueue(1)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()

# print(param_1, param_2, param_3, param_4, param_5, param_6)



# class Node:
#     def __init__(self, value, nextNode = None):
#         self.value = value
#         self.next = nextNode

# class MyCircularQueue:
#     def __init__(self, k: int):
#         self.head = None
#         self.tail = None
#         self.count = 0
#         self.capacity = k
    
#     def isEmpty(self) -> bool:
#         return self.count == 0

#     def isFull(self) -> bool:
#         return self.count == self.capacity
    
#     def enQueue(self, value: int) -> bool:
#         if self.isFull():
#             return False
#         elif self.isEmpty():
#             self.head = Node(value)
#             self.tail = self.head
#         else:
#             newNode = Node(value)
#             self.tail.next = newNode
#             self.tail = newNode
#         self.count += 1
#         return True
    
#     def deQueue(self) -> bool:
#         if self.isEmpty():
#             return False
#         self.head = self.head.next
#         self.count -= 1
#         return True
    
#     def Front(self) -> int:
#         if self.isEmpty():
#             return -1
#         return self.head.value

#     def Rear(self) -> int:
#         if self.isEmpty():
#             return -1
#         return self.tail.value




# Stack

# class MinStack:

#     def __init__(self):
#         self.stack = []

#     def push(self, val: int) -> None:
#         if not self.stack:
#             self.stack.append([val, val])
#         else:
#             curr_min = self.stack[-1][1]
#             self.stack.append([val, min(val, curr_min)])

#     def pop(self) -> None:
#         self.stack.pop()      

#     def top(self) -> int:
#         return self.stack[-1][0]

#     def getMin(self) -> int:
#         return self.stack[-1][1]




# Heap

    # class MinHeap:
    #     def __init__(self, heapSize):
    #         self.heapSize = heapSize
    #         self.minHeap = [0] * (heapSize + 1) 
    #         self.realSize = 0
    #     def add(self, element):
    #         self.realSize += 1
    #         if self.realSize > self.heapSize:
    #             print("Added too many elements")
    #             self.realSize -= 1
    #             return 
    #         self.minHeap[self.realSize] = element
    #         index = self.realSize
    #         parent = index // 2
    #         while self.minHeap[index] < self.minHeap[parent] and index > 1:
    #             self.minHeap[parent], self.minHeap[index] = self.minHeap[index], self.minHeap[parent]
    #             index = parent
    #             parent = index // 2
    #     def peek(self):
    #         return self.minHeap[1]
    #     def pop(self):
    #         if self.realSize < 1:
    #             print("Don`t have any element!")
    #             return 
    #         else:
    #             removedElement = self.minHeap[1]
    #             self.minHeap[1] = self.minHeap[self.real.size]
    #             self.realSize -= 1
    #             index = 1
    #             while index <= self.realSize // 2:
    #                 left = index * 2
    #                 right = index * 2 + 1
    #                 if self.minHeap[index] > self.minHeap[left] or self.minHeap[index] > self.minHeap[right]:
    #                     if self.minHeap[left] < self.minHeap[right]:
    #                         self.minHeap[left], self.minHeap[index] = self.minHeap[index], self.minHeap[left]
    #                         index = left
    #                     else:
    #                         self.minHeap[right], self.minHeap[index] = self.minHeap[index], self.minHeap[right]
    #                         index = right
    #                 else:
    #                     break
    #         return removedElement
    #     def size(self):
    #         return self.realSize
        
    # minHeap = MinHeap(5)
    # minHeap.add(14)
    # minHeap.add(41)
    # minHeap.add(1)
    # minHeap.add(10)
    # print(minHeap)


# class MaxHeap:
#     def __init__(self, heapSize):
#         self.heapSize = heapSize
#         self.maxHeap = [0] * (heapSize + 1)
#         self.realSize = 0
#     def add(self, element):
#         self.realSize += 1
#         if self.realSize > self.heapSize:
#             print("Can`t do it, there are too many elements!")
#             self.realSize -= 1
#             return 
#         self.maxHeap[self.realSize] = element
#         index = self.realSize
#         parent = index // 2
#         while self.maxHeap[index] > self.maxHeap[parent] and index > 1:
#             self.maxHeap[parent], self.maxHeap[index] = self.maxHeap[index], self.maxHeap[parent]
#             index = parent
#             parent = index // 2
#     def peek(self):
#         return self.maxHeap[1]
#     def pop(self):
#         if self.realSize < 1:
#             print("There is no element!")
#             return
#         else:
#             removedElement = self.maxHeap[1]
#             self.maxHeap[1] = self.maxHeap[self.realSize]
#             self.realSize -= 1
#             index = 1
#             while index <= self.realSize // 2:
#                 left = index * 2
#                 right = index * 2 + 1
#                 if self.maxHeap[index] < self.maxHeap[left] or self.maxHeap[index] < self.maxHeap[right]:
#                     if self.maxHeap[left] > self.maxHeap[right]:
#                         self.maxHeap[left], self.maxHeap[index] = self.maxHeap[index], self.maxHeap[left]
#                         index = left
#                     else:
#                         self.maxHeap[right], self.maxHeap[index] = self.maxHeap[index], self.maxHeap[right]
#                         index = right
#                 else:
#                     break
#         return removedElement
#     def size(self):
#         return self.realSize

# maxHeap = MaxHeap(5)
# maxHeap.add(1)
# maxHeap.add(2)
# maxHeap.add(3)
# maxHeap.add(5)
# maxHeap.add(4)
# print(maxHeap)
# print(maxHeap.peek())
# print(maxHeap.pop())
# print(maxHeap.pop())
# print(maxHeap.pop())
# maxHeap.add(4)
# maxHeap.add(5)
# print(maxHeap)
