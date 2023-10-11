# A linked list of length n is given such that each node contains an additional random pointer, which could point to any node 
# in the list, or null.

# Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its 
# value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point 
# to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state.
# None of the pointers in the new list should point to nodes in the original list.

# For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes
#  x and y in the copied list, x.random --> y.

# Return the head of the copied linked list.

# The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] 
# where:

    # val: an integer representing Node.val
    # random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.

# Your code will only be given the head of the original linked list.


class Node:
    def __init__(self, x, next = None, random = None):
        self.val = x
        self.next = next
        self.random = random

def copyRandomList(head):
    if not head:
        return None
    
    curr_node = head
    while curr_node:
        new_node = Node(curr_node.val)
        
        # A->A'->B->B'->C->C'
        new_node.next = curr_node.next
        curr_node.next = new_node
        curr_node = new_node.next

    curr_node = head
    while curr_node:
        curr_node.next.random = curr_node.random.next if curr_node.random else None
        curr_node = curr_node.next.next

    old_list = head # A->B->C
    new_list = head.next # A'->B'->C'
    new_head = head.next
    while old_list:
        old_list.next = old_list.next.next
        new_list.next = new_list.next.next if new_list.next else None

        old_list = old_list.next
        new_list = new_list.next

    return new_head


def copyRandomList2(head):
    if not head:
        return None
    
    deep_copy = {}
    curr_node = head
    while curr_node:
        deep_copy[curr_node] = Node(curr_node.val)
        curr_node = curr_node.next

    curr_node = head 
    while curr_node:
        deep_copy[curr_node].next = deep_copy.get(curr_node.next)
        deep_copy[curr_node].random = deep_copy.get(curr_node.random)
        curr_node = curr_node.next

    return deep_copy[head]