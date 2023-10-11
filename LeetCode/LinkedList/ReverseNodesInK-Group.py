# Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not
# a multiple of k then left-out nodes, in the end, should remain as it is.

# You may not alter the values in the list's nodes, only nodes themselves may be changed.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseKGroup(head, k):
    dummy = ListNode(0, head)
    groupPrev = dummy

    while True:
        kth = getkth(groupPrev, k)
        if not kth:
            break
        groupNext = kth.next

        # reversing the group of length k
        prev, curr = kth.next, groupPrev.next
        while curr != groupNext:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        temp = groupPrev.next
        groupPrev.next = kth
        groupPrev = temp

    return dummy.next

def getkth(node, k):
    while node and k > 0:
        node = node.next
        k -= 1
    return node


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

k = 3

reversed_head = reverseKGroup(head, k)

while reversed_head:
    print(reversed_head.val, end = " ")
    reversed_head = reversed_head.next