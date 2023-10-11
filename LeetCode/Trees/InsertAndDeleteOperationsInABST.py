class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BST:
    def __init__(self, root):
        self.root = root
        self.head = ListNode(root.val)
        self.tail = ListNode(root.val)
        self.capacity = 0
        
    def inOrder(self, root):
        return self.inOrder(root.left) + [root.val] + self.inOrder(root.right) if root else []
    
    def kthSmallest(self, k):
        if k > self.capacity:
            return -1
        curr = self.head
        k -= 1
        while k:
            curr = curr.next
            k -= 1
        return curr.val
    
    def display(self):
        curr = self.head
        while curr:
            print(curr.val, end=" ")
            curr = curr.next

    def insertIntoLinkedList(self, val):
        newNode = ListNode(val)
        self.capacity += 1

        if self.head is None:
            self.head = newNode
            self.tail = newNode
            return
        
        if val <= self.head.val:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
            return
        
        curr = self.head
        
        while curr.next is not None and val > curr.next.val:
            curr = curr.next
        
        if curr.next is None:
            curr.next = newNode
            newNode.prev = curr
            self.tail = newNode
        else:
            newNode.next = curr.next
            newNode.prev = curr
            curr.next.prev = newNode
            curr.next = newNode

    def deleteNodeFromLinkedList(self, val):
        if self.head is None:
            return 
        
        self.capacity -= 1
        curr = self.head

        while curr is not None:
            if curr.val == val:
                if curr == self.head:
                    self.head = curr.next
                    if self.head is not None:
                        self.head.prev = None
                    else:
                        self.tail = None
                else:
                    curr.prev.next = curr.next
                    if curr.next is not None:
                        curr.next.prev = curr.prev
                    else:
                        self.tail = curr.prev
                return
            curr = curr.next

    def insertIntoBST(self, root, val):
        
        def DFS(root, val):
            if not root:
                return TreeNode(val)
            if val > root.val:
                root.right = DFS(root.right, val)
            else: 
                root.left = DFS(root.left, val)
            return root
        
        self.insertIntoLinkedList(val)
        DFS(root, val)
    
    def deleteNodeFromBST(self, root, val):

        def DFS(root, val):
            if not root:
                return None
            
            if val > root.val:
                root.right = DFS(root.right, val)
            elif val < root.val:
                root.left = DFS(root.left, val)
            else:
                if not (root.left or root.right):
                    root = None
                elif root.right:
                    root.val = self.successor(root)
                    root.right = DFS(root.right, root.val)
                else:
                    root.val = self.predecessor(root)
                    root.left = DFS(root.left, root.val)

            return root
        
        self.deleteNodeFromLinkedList(val)
        DFS(root, val)
    
    def successor(self, root):
        root = root.right
        while root.left:
            root = root.left
        return root.val
    
    def predecessor(self, root):
        root = root.left
        while root.right:
            root = root.right
        return root.val

if __name__ == '__main__':
    root = TreeNode(4)
    bst = BST(root)
    bst.insertIntoBST(root, 5)
    bst.insertIntoBST(root, 1)
    bst.insertIntoBST(root, 2)
    bst.insertIntoBST(root, 3)
    bst.insertIntoBST(root, 7)

    print(bst.inOrder(root))
    print(bst.display())

    bst.deleteNodeFromBST(root, 4)

    print(bst.inOrder(root))
    print(bst.display())

    print(bst.kthSmallest(10))