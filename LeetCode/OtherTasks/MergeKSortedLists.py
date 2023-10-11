# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists):
    if not lists:
        return None
    
    while len(lists) > 1:
        mergedList = []

        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i + 1] if i + 1 < len(lists) else None
            mergedList.append(mergeLists(l1, l2))
        
        lists = mergedList
    
    return lists[0]

def mergeLists(l1, l2):
    dummy = tail = ListNode(0)
    
    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2 
            l2 = l2.next
        tail = tail.next
    tail.next = l1 if l1 else l2

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