# A red-black tree T is a binary search tree having following five additional properties (invariants).

    # Every node in T is either red or black.
    # The root node of T is black.
    # Every NULL node is black. (NULL nodes are the leaf nodes. They do not contain any keys. When we search for a key that 
                            #    is not present in the tree, we reach the NULL node.)
    # If a node is red, both of its children are black. This means no two nodes on a path can be red nodes.
    # Every path from a root node to a NULL node has the same number of black nodes.


# Insertion

# To insert a node K into a red-black tree T, we do the following.

    # We insert K using an ordinary BST insertion operation.
    # We color K red.
    # We check if the insertion violated the red-black tree properties. If it did, we fix it.


class RBNode:

    BLACK = False
    RED = True
    
    def __init__(self, val):
        self.val = val
        self.parent = None
        self.left = None
        self.right = None
        self.color = RBNode.BLACK # False -> black, True -> red


class NILNode(RBNode):

    def __init__(self):
        super().__init__(-1)


class RBTree:

    def __init__(self):
        self.root = None

    def search(self, val):
        curr_node = self.root

        while curr_node != None:
            if curr_node.val == val:
                return curr_node
            elif curr_node.val > val:
                curr_node = curr_node.left 
            else:
                curr_node = curr_node.right
        
        return -1
    
    # -- Insertion ----------------------------------------------------------------------------------
    
    def insert(self, val):
        curr_node = self.root
        parent = None

        while curr_node != None:
            parent = curr_node
            if curr_node.val > val:
                curr_node = curr_node.left
            elif curr_node.val < val:
                curr_node = curr_node.right
            else:
                raise ValueError("BST already has one of the same child, the second is not needed.")
            
        new_node = RBNode(val)
        new_node.color = RBNode.RED
        if parent is None:
            self.root = new_node
        elif parent.val > val:
            parent.left = new_node
        else:
            parent.right = new_node
        new_node.parent = parent

        self.__fix_insertion(new_node)

    def __fix_insertion(self, node):
        parent = node.parent

        # Case 1: Parent is null, we've reached the root, the end of the recursion
        if parent is None:
            node.color = RBNode.BLACK
            return 

        # Parent is black --> nothing to do
        if parent.color == RBNode.BLACK:
            return
        
        # From here on, parent is red
        grandparent = parent.parent
        
        # Case 2:
        # Get the uncle (may be null/nil, in which case its color is BLACK)
        uncle = self.__getUncle(parent)

        # Uncle is red -> recolor (parent, uncle) and grandparent
        if uncle is not None and uncle.color == RBNode.RED:
            parent.color = RBNode.BLACK
            uncle.color = RBNode.BLACK
            grandparent.color = RBNode.RED

            # Call recursively for grandparent, which is now red.
            # It might be root or have a red parent, in which case we need to fix more...
            self.__fix_insertion(grandparent)
        
        # Parent is left child of grandparent
        elif parent == grandparent.left:
            # Case 4a: Uncle is black and node is left->right "inner child" of its grandparent
            if node == parent.right:
                self.____rotate_left(parent)
            
                # Let "parent" point to the new root node of the rotated sub-tree.
                parent = node

            # Case 5a: Uncle is black and node is left->left "outer child" of its grandparent
            self.__rotate_right(grandparent)

            # Recolor original parent and grandparent
            parent.color = RBNode.BLACK
            grandparent.color = RBNode.RED

        # Parent is right child of grandparent
        else:
            # Case 4b: Uncle is black and node is right->left "inner child" of its grandparent
            if node == parent.left:
                self.__rotate_right(parent)

                parent = node
            
            # Case 5b: Uncle is black and node is right->right "outer child" of its grandparent
            self.__rotate_left(grandparent)

            parent.color = RBNode.BLACK
            grandparent.color = RBNode.RED

    def __getUncle(self, parent):
        grandparent = parent.parent

        if grandparent.left == parent:
            return grandparent.right
        elif grandparent.right == parent:
            return grandparent.left
        else:
            raise ValueError("The parent was found in the garden.")
        
    # -- Deletion -----------------------------------------------------------------------------------

    # If the node to be deleted has no children, we simply remove it.
    # If the node to be deleted has one child, we remove the node and let its single child move up to its position.
    # If the node to be deleted has two children, we copy the content (not the color!) of the in-order successor of the 
    # right child into the node to be deleted and then delete the in-order successor according to rule 1 or 2 
    # (the in-order successor has at most one child by definition).

    def delete(self, val):
        curr_node = self.root

        while curr_node and curr_node.val != val:
            if curr_node.val > val:
                curr_node = curr_node.left
            else:
                curr_node = curr_node.right

        if not curr_node:
            return -1
        
        movedUpNode = None 
        deletedNodeColor = RBNode.BLACK

        # Node has zero or one child
        if not curr_node.left or not curr_node.right:
            movedUpNode = self.__deleteNodeWithZeroOrOneChild(curr_node)
            deletedNodeColor = curr_node.color

        # Node has two children
        else:
            # Find minimum node of right subtree ("inorder successor" of current node)
            inOrderSuccessor = self.successor(curr_node.right)

            # Copy inorder successor's data to current node (keep its color!)
            curr_node.val = inOrderSuccessor.val
            movedUpNode = self.__deleteNodeWithZeroOrOneChild(inOrderSuccessor)
            deletedNodeColor = inOrderSuccessor.color

        if not deletedNodeColor:
            self.__fix_deletion(movedUpNode)

            # Remove the temporary NIL node
            if isinstance(movedUpNode, NILNode):
                self.__replaceParentsChild(movedUpNode.parent, movedUpNode, None)

    def __deleteNodeWithZeroOrOneChild(self, node):
        # Node has ONLY a left child --> replace by its left child
        if node.left:
            self.__replaceParentsChild(node.parent, node, node.left)
            return node.left # moved-up node

        # Node has ONLY a right child --> replace by its right child
        elif node.right:
            self.__replaceParentsChild(node.parent, node, node.right)
            return node.right # moved-up node
        
        # Node has no children -->
        # * node is red --> just remove it
        # * node is black --> replace it by a temporary NIL node (needed to fix the R-B rules)
        else:
            newChild = NILNode() if node.color == RBNode.BLACK else None
            self.__replaceParentsChild(node.parent, node, newChild)
            return newChild
    
    def successor(self, node):
        while node.left:
            node = node.left
        return node

    # Case 1: Deleted node is the root
    # Case 2: Sibling is red
    # Case 3: Sibling is black and has two black children, parent is red
    # Case 4: Sibling is black and has two black children, parent is black
    # Case 5: Sibling is black and has at least one red child, "outer nephew" is black
    # Case 6: Sibling is black and has at least one red child, "outer nephew" is red
    def __fix_deletion(self, node):
        # Case 1: Examined node is root, end of recursion
        if node == self.root:
            node.color = RBNode.BLACK
            return 

        sibling = self.__getSibling(node)

        # Case 2: Red sibling
        if sibling.color == RBNode.RED:
            self.__handleRedSibling(node, sibling)
            sibling = self.__getSibling(node) # Get new sibling for fall-through to cases 3-6

        # Cases 3+4: Black sibling with two black children
        if self.__isBlack(sibling.left) and self.__isBlack(sibling.right):
            sibling.color = RBNode.RED

            # Case 3: Black sibling with two black children + red parent
            if node.parent.color == RBNode.RED:
                node.parent.color = RBNode.BLACK

            # Case 4: Black sibling with two black children + black parent
            else:
                self.__fix_deletion(node.parent)

        # Case 5+6: Black sibling with at least one red child
        else:
            self.__handleBlackSiblingWithAtLeastOneRedChild(node, sibling)
        
    def __getSibling(self, node):
        parent = node.parent

        if node == parent.left:
            return parent.right
        elif node == parent.right:
            return parent.left
        else:
            raise ValueError("The node is asian and his parents are black.")
        
    def __isBlack(self, node):
        return node == None or node.color == RBNode.BLACK
    
    def __handleRedSibling(self, node, sibling):
        # Recolor...
        sibling.color = RBNode.BLACK
        node.parent.color = RBNode.RED

        # ... and rotate
        if node == node.parent.left:
            self.__rotate_left(node.parent)
        else:
            self.__rotate_right(node.parent)

    def __handleBlackSiblingWithAtLeastOneRedChild(self, node, sibling):
        nodeIsLeftChild = node == node.parent.left

        # Case 5: Black sibling with at least one red child + "outer nephew" is black
        # --> Recolor sibling and its child, and rotate around sibling
        if nodeIsLeftChild and self.__isBlack(sibling.right):
            sibling.left.color = RBNode.BLACK
            sibling.color = RBNode.RED
            self.__rotate_right(sibling)
            sibling = node.parent.right 
        elif not nodeIsLeftChild and self.__isBlack(sibling.left):
            sibling.right.color = RBNode.BLACK
            sibling.color = RBNode.RED
            self.__rotate_left(sibling)
            sibling = node.parent.left

        # Fall-through to case 6...

        # Case 6: Black sibling with at least one red child + "outer nephew" is red
        # --> Recolor sibling + parent + sibling's child, and rotate around parent
        sibling.color = node.parent.color
        node.parent.color = RBNode.BLACK
        if nodeIsLeftChild:
            sibling.right.color = RBNode.BLACK
            self.__rotate_left(node.parent)
        else:
            sibling.left.color = RBNode.BLACK
            self.__rotate_right(node.parent)

    # -- Helpers for insertion and deletion ---------------------------------------------------------

    def __rotate_right(self, node):
        parent = node.parent
        leftChild = node.left

        node.left = leftChild.right
        if leftChild.right is not None:
            leftChild.right.parent = node
        
        leftChild.right = node
        node.parent = leftChild

        self.__replaceParentsChild(parent, node, leftChild)

    def __rotate_left(self, node):
        parent = node.parent
        rightChild = node.right

        node.right = rightChild.left
        if rightChild.left is not None:
            rightChild.left.parent = node

        rightChild.left = node
        node.parent = rightChild

        self.__replaceParentsChild(parent, node, rightChild)

    def __replaceParentsChild(self, parent, oldChild, newChild):
        if parent is None:
            self.root = newChild
        elif parent.left == oldChild:
            parent.left = newChild
        elif parent.right == oldChild:
            parent.right = newChild
        else:
            raise ValueError("The node is adopted!")
        

        if newChild is not None:
            newChild.parent = parent

    # -- Printing the tree --------------------------------------------------------------------------

    def inOrder(self, node):
        if not node:
            return 
        self.inOrder(node.left)
        print(node.val)
        self.inOrder(node.right)


T = RBTree()
T.insert(432)
T.insert(765432)
T.insert(1234)
T.insert(91243565)
T.insert(12323)
T.insert(565324)
T.insert(51233)
T.insert(1)
T.insert(51324564)
T.insert(13247)
T.insert(1324)
T.insert(13247130)
T.inOrder(T.root)

T.delete(51233)