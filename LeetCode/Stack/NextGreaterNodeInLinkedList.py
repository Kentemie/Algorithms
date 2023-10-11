# You are given the head of a linked list with n nodes.

# For each node in the list, find the value of the next greater node. That is, for each node, find the value of the first 
# node that is next to it and has a strictly larger value than it.

# Return an integer array answer where answer[i] is the value of the next greater node of the ith node (1-indexed).
# If the ith node does not have a next greater node, set answer[i] = 0.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseLinkedList(head):
    prev = None
    curr = head
    n = 0
    while curr:
        nextNode = curr.next
        curr.next = prev
        prev = curr
        curr = nextNode
        n += 1
    return prev, n

def nextLargerNodes(head):
    reversed_head, n = reverseLinkedList(head)
    stack = [reversed_head.val]
    reversed_head = reversed_head.next
    res = [0] * n
    i = n - 2

    while reversed_head:
        while stack and stack[-1] <= reversed_head.val:
            stack.pop()
        if stack:
            res[i] = stack[-1]
        stack.append(reversed_head.val)
        i -= 1
        reversed_head = reversed_head.next
    
    return res


head = ListNode(2)
head.next = ListNode(7)
head.next.next = ListNode(4)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(5)

print(nextLargerNodes(head))
