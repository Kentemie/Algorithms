# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.

from heapq import heappop, heappush

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Pair:
    def __init__(self, val, node):
        self.val = val
        self.node = node
    
    def __lt__(self, other):
        return self.val < other.val or self.val == other.val

def mergeKLists(lists):
    PQ = []
    for lst in lists:
        if lst:
            heappush(PQ, Pair(lst.val, lst))

    dummy = tail = ListNode(0)
    while PQ:
        lst = heappop(PQ)
        tail.next = ListNode(lst.val)
        tail = tail.next
        lst.node = lst.node.next
        if lst.node:
            heappush(PQ, Pair(lst.node.val, lst.node))

    return dummy.next


l1 = ListNode(1)
l1.next = ListNode(4)
l1.next.next = ListNode(5)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

l3 = ListNode(2)
l3.next = ListNode(6)

lists = [l1, l2, l3]

l4 = mergeKLists(lists)

while l4:
    print(l4.val, end = " ")
    l4 = l4.next