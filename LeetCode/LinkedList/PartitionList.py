# Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

# You should preserve the original relative order of the nodes in each of the two partitions.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def partition(head, x):
    dummy1 = dummy1_node = ListNode(-101)
    dummy2 = dummy2_node = ListNode(-101)

    while head:
        if head.val < x:
            dummy1_node.next = head
            dummy1_node = dummy1_node.next
        else:
            dummy2_node.next = head
            dummy2_node = dummy2_node.next
        head = head.next
    
    dummy2_node.next = None
    dummy1_node.next = dummy2.next

    return dummy1.next



head = ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2))))))
x = 3

new_head = partition(head, x)

while new_head:
    print(new_head.val, end=" ")
    new_head = new_head.next