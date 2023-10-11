# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def isPalindrome(head):
    if not head:
        return True
    
    firstHalfEnd = endOfTheFirstHalf(head)
    reversedSecondHalfStart = reverse(firstHalfEnd.next)

    res = True
    firstHalf = head
    secondHalf = reversedSecondHalfStart

    while res and secondHalf:
        if firstHalf.val != secondHalf.val:
            res = False
        firstHalf = firstHalf.next
        secondHalf = secondHalf.next

    firstHalfEnd.next = reverse(reversedSecondHalfStart)

    return res

def endOfTheFirstHalf(head):
    hare = head
    tortoise = head

    while hare.next and hare.next.next:
        hare = hare.next.next
        tortoise = tortoise.next

    return tortoise

def reverse(head):
    prev = None
    curr = head

    while curr:
        nextNode = curr.next
        curr.next = prev
        prev = curr
        curr = nextNode

    return prev

# head = ListNode(1)
# head.next = ListNode(2)
# head.next.next = ListNode(2)
# head.next.next.next = ListNode(1)


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)
head.next.next.next.next.next.next = ListNode(7)
head.next.next.next.next.next.next.next = ListNode(8)
head.next.next.next.next.next.next.next.next = ListNode(9)
head.next.next.next.next.next.next.next.next.next = ListNode(10)


print(isPalindrome(head))