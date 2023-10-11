# Design and implement a data structure for a Least Frequently Used (LFU) cache.

# Implement the LFUCache class:

    # LFUCache(int capacity) Initializes the object with the capacity of the data structure.
    # int get(int key) Gets the value of the key if the key exists in the cache. Otherwise, returns -1.
    # void put(int key, int value) Update the value of the key if present, or inserts the key if not already present. When the 
    # cache reaches its capacity, it should invalidate and remove the least frequently used key before inserting a new item.
    # For this problem, when there is a tie (i.e., two or more keys with the same frequency), the least recently used key would
    # be invalidated.

# To determine the least frequently used key, a use counter is maintained for each key in the cache. The key with the smallest
# use counter is the least frequently used key.

# When a key is first inserted into the cache, its use counter is set to 1 (due to the put operation). The use counter for 
# a key in the cache is incremented either a get or put operation is called on it.

# The functions get and put must each run in O(1) average time complexity.

class ListNode:

    def __init__(self, key, value):
        self.key = key 
        self.value = value
        self.freq = 1
        self.next = None
        self.prev = None


class DoublyLinkedList:

    def __init__(self):
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.length = 0

    def add(self, node):
        real_tail = self.tail.prev
        real_tail.next = node
        node.prev = real_tail
        node.next = self.tail 
        self.tail.prev = node
        self.length += 1

    def remove(self, node):
        node.prev.next = node.next 
        node.next.prev = node.prev
        self.length -= 1


class LFUCache:
    
    def __init__(self, capacity):
        self.capacity = capacity
        self.minFreq = 0
        self.cache = {}         # key: node(key, value, freq)
        self.frequencies = {}   # freq: DLL
    
    def put(self, key, value):
        if key in self.cache:
            self.update(key, value)
        else:
            if len(self.cache) == self.capacity:
                lfu_node = self.frequencies[self.minFreq].head.next
                self.frequencies[self.minFreq].remove(lfu_node)
                
                if self.frequencies[self.minFreq].length == 0:
                    del self.frequencies[self.minFreq]
                del self.cache[lfu_node.key]
            
            new_node = ListNode(key, value)
            self.cache[key] = new_node
            self.minFreq = 1
            self.insert(new_node)

    def get(self, key):
        if key not in self.cache:
            return -1

        return self.update(key)
    
    def insert(self, node):
        if node.freq not in self.frequencies:
            self.frequencies[node.freq] = DoublyLinkedList()
        
        self.frequencies[node.freq].add(node)

    def update(self, key, value=None):
        node = self.cache[key]

        if value:
            node.value = value

        old_freq = node.freq
        node.freq += 1
        self.frequencies[old_freq].remove(node)
        
        if self.minFreq == old_freq and self.frequencies[old_freq].length == 0:
            self.minFreq += 1
            del self.frequencies[old_freq]
        
        self.insert(node)

        return node.value


obj = LFUCache(2)

obj.put(1,1)
obj.put(2,2)
print(obj.get(1))
obj.put(3,3)
print(obj.get(2))
print(obj.get(3))
obj.put(4,4)
print(obj.get(1))
print(obj.get(3))
print(obj.get(4))