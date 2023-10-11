# Given the head of a linked list, remove the nth node from the end of the list and return its head.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Maintaining N nodes apart between first and second pointers

def removeNthFromEnd(head, n):
    node = ListNode(0)
    node.next = head

    first = node
    second = node

    for _ in range(n + 1):
        first = first.next

    while first:
        first = first.next
        second = second.next

    second.next = second.next.next

    return node.next

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

newNode = removeNthFromEnd(head, 3)

while newNode:
    print(newNode.val, end = " ")
    newNode = newNode.next