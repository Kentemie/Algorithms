# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in 
# reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    res = ListNode(-1)
    curr = res
    carry = 0

    while l1 or l2:
        l1Val = l1.val if l1 else 0
        l2Val = l2.val if l2 else 0

        _sum = (l1Val + l2Val + carry) % 10
        carry = (l1Val + l2Val + carry) // 10

        newNode = ListNode(_sum)
        curr.next = newNode
        curr = newNode

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    if carry:
        newNode = ListNode(carry)
        curr.next = newNode

    return res.next

# l1 = ListNode(2)
# l1.next = ListNode(4)
# l1.next.next = ListNode(3)

# l2 = ListNode(5)
# l2.next = ListNode(6)
# l2.next.next = ListNode(4)

# 2 -> 4 -> 3
#             +
# 5 -> 6 -> 4
# -----------
# 7 -> 0 -> 8

l1 = ListNode(9)
l1.next = ListNode(9)
l1.next.next = ListNode(9)
l1.next.next.next = ListNode(9)
l1.next.next.next.next = ListNode(9)
l1.next.next.next.next.next = ListNode(9)
l1.next.next.next.next.next.next = ListNode(9)

l2 = ListNode(9)
l2.next = ListNode(9)
l2.next.next = ListNode(9)
l2.next.next.next = ListNode(9)

# 9 -> 9 -> 9 -> 9 -> 9 -> 9 -> 9
#                                 + 
# 9 -> 9 -> 9 -> 9
# -------------------------------
# 8 -> 9 -> 9 -> 9 -> 0 -> 0 -> 0 -> 1 

l3 = addTwoNumbers(l1, l2)

while l3:
    print(l3.val, end = " ")
    l3 = l3.next