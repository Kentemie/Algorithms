# Given the head of a linked list, return the list after sorting it in ascending order.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def sortList(head):
    if not head or not head.next:
        return head
    
    mid = getMid(head)
    left = sortList(head)
    right = sortList(mid)
    return merge(left, right)

def merge(list1, list2):
    dummy = ListNode()
    tail = dummy

    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next
    
    tail.next = list1 if list1 else list2 

    return dummy.next
    
def getMid(head):
    midPrev = None

    while head and head.next:
        midPrev = midPrev.next if midPrev else head
        head = head.next.next

    mid = midPrev.next
    midPrev.next = None
    return mid


head = ListNode(-1, ListNode(5, ListNode(3, ListNode(4, ListNode(0)))))

new_head = sortList(head)

while new_head:
    print(new_head.val, end = " ")
    new_head = new_head.next