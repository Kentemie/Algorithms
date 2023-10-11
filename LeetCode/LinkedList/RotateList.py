# Given the head of a linked list, rotate the list to the right by k places.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def rotateRight(head, k):
    if not head:
        return None 
    if not head.next:
        return head 
    
    old_tail = head
    n = 1
    while old_tail.next:
        old_tail = old_tail.next
        n += 1
    old_tail.next = head

    new_tail = head 
    for i in range(n - k % n - 1):
        new_tail = new_tail.next
    new_head = new_tail.next

    new_tail.next = None

    return new_head

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
k = 2

print(rotateRight(head, k))