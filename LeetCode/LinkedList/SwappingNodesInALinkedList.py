# You are given the head of a linked list, and an integer k.

# Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node
# from the end (the list is 1-indexed).

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapNodes(head, k):
    n = 0
    dummy = head
    endNode = None

    while dummy:
        n += 1
        if endNode != None:
            endNode = endNode.next
        if n == k:
            frontNode = dummy
            endNode = head
        dummy = dummy.next

    frontNode.val, endNode.val = endNode.val, frontNode.val

    return head

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

k = 2

swaped_head = swapNodes(head, k)

while swaped_head:
    print(swaped_head.val, end = " ")
    swaped_head = swaped_head.next