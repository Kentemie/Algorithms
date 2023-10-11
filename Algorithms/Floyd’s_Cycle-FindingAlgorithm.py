# This algorithm is used to find a loop in a linked list. It uses two pointers one moving twice as fast as the other one. 
# The faster one is called the faster pointer and the other one is called the slow pointer.

# Follow the steps below to solve the problem:

    # Traverse linked list using two pointers.
    # Move one pointer(slow_p) by one and another pointer(fast_p) by two.
    # If these pointers meet at the same node then there is a loop. If pointers do not meet then the linked list 
    # doesn’t have a loop.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def detectLoop(head):
    hare = tortoise = head
    while hare and hare.next:
        tortoise = tortoise.next
        hare = hare.next.next
        if tortoise == hare:
            break

    if hare != tortoise:
        return None
    
    tortoise = head
    while tortoise != hare:
        tortoise = tortoise.next
        hare = hare.next

    return tortoise

head = ListNode(50)
head.next = ListNode(40)
head.next.next = ListNode(30)
head.next.next.next = ListNode(20)
head.next.next.next.next = ListNode(10)

temp = head
while temp.next:
    temp = temp.next

temp.next = head.next

loopStart = detectLoop(head)
if loopStart:
    print(f"Loop does exists and starts from {loopStart.val}.")
else:
    print("There is no loop.")