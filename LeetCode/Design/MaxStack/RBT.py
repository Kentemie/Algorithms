class Node:

    black = False
    red = True

    def __init__(self, *args):
        self.val = args[0]
        self.parent = None
        self.left = None
        self.right = None
        self.color = Node.black

class NILNode(Node):

    def __init__(self):
        super().__init__([-1, -1])


class RedBlackTree:

    def __init__(self):
        self.root = None

    def top(self):
        curr_node = self.root
        while curr_node.right:
            curr_node = curr_node.right
        return curr_node

    
    # -- Insertion ---------------------------------------------------------------------------------- #

    def insert(self, *args):
        val = args[0]
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
        
        new_node = Node(val)
        new_node.color = Node.red

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

        if parent is None:
            node.color = Node.black
            return
        
        if parent.color == Node.black:
            return
        
        grandparent = parent.parent
        uncle = self.__get_uncle(parent)

        if uncle is not None and uncle.color == Node.red:
            parent.color = Node.black
            uncle.color = Node.black
            grandparent.color = Node.red

            self.__fix_insertion(grandparent)
        elif parent == grandparent.left:
            if node == parent.right:
                self.__rotate_left(parent)
                parent = node
            self.__rotate_right(grandparent)
            parent.color = Node.black
            grandparent.color = Node.red
        else:
            if node == parent.left:
                self.__rotate_right(parent)
                parent = node
            self.__rotate_left(grandparent)
            parent.color = Node.black
            grandparent.color = Node.red
    
    def __get_uncle(self, parent):
        grandparent = parent.parent

        if grandparent.left == parent:
            return grandparent.right
        elif grandparent.right == parent:
            return grandparent.left
        else:
            raise ValueError("The parent was found in the garden.")
        
    # -- Deletion ----------------------------------------------------------------------------------- #

    def pop(self):
        curr_node = self.top()
        
        self.delete(curr_node, "Need to remove the last node.")

        return curr_node.val

    def delete(self, *args):
        if len(args) > 1:
            curr_node = args[0]
        else:
            val = args[0]
            curr_node = self.root

            while curr_node and curr_node.val != val:
                if curr_node.val > val:
                    curr_node = curr_node.left
                else:
                    curr_node = curr_node.right

            if curr_node is None:
                return -1
            
        moved_up_node = None
        deleted_node_color = Node.black

        if curr_node.left is None or curr_node.right is None:
            moved_up_node = self.__delete_node_with_zero_or_one_child(curr_node)
            deleted_node_color = curr_node.color
        else:
            in_order_successor = self.__successor(curr_node.right)

            curr_node.val = in_order_successor.val
            moved_up_node = self.__delete_node_with_zero_or_one_child(in_order_successor)
            deleted_node_color = in_order_successor.color

        if deleted_node_color == Node.black:
            self.__fix_deletion(moved_up_node)

            if isinstance(moved_up_node, NILNode):
                self.__replace_parents_child(moved_up_node.parent, moved_up_node, None)
    
    def __delete_node_with_zero_or_one_child(self, node):
        if node.left:
            self.__replace_parents_child(node.parent, node, node.left)
            return node.left
        elif node.right:
            self.__replace_parents_child(node.parent, node, node.right)
            return node.right
        else:
            new_child = None
            if node.color == Node.black:
                new_child = NILNode()
            self.__replace_parents_child(node.parent, node, new_child)
            return new_child
        
    def __successor(self, node):
        while node.left:
            node = node.left
        return node
    
    def __fix_deletion(self, node):
        if node == self.root:
            node.color = Node.black
            return 
        
        sibling = self.__get_sibling(node)

        if sibling.color == Node.red:
            self.__handle_red_sibling(node, sibling)
            sibling = self.__get_sibling(node)

        if self.__is_black(sibling.left) and self.__is_black(sibling.right):
            sibling.color = Node.red

            if node.parent.color == Node.red:
                node.parent.color = Node.black
            else:
                self.__fix_deletion(node.parent)
        
        else:
            self.__handle_black_sibling_with_at_least_one_red_child(node, sibling)

    def __get_sibling(self, node):
        parent = node.parent 

        if node == parent.left:
            return parent.right
        elif node == parent.right:
            return parent.left
        else:
            raise ValueError("The node is asian and his parents are black.")
    
    def __is_black(self, node):
        return node == None or node.color == Node.black
    
    def __handle_red_sibling(self, node, sibling):
        sibling.color = Node.black
        node.parent.color = Node.red

        if node == node.parent.left:
            self.__rotate_left(node.parent)
        else:
            self.__rotate_right(node.parent)

    def __handle_black_sibling_with_at_least_one_red_child(self, node, sibling):
        node_is_left_child = node == node.parent.left

        if node_is_left_child and self.__is_black(sibling.right):
            sibling.left.color = Node.black     
            sibling.color = Node.red
            self.__rotate_right(sibling)
            sibling = node.parent.right
        elif not node_is_left_child and self.__is_black(sibling.left):
            sibling.right.color = Node.black
            sibling.color = Node.red
            self.__rotate_left(sibling)
            sibling = node.parent.left

        sibling.color = node.parent.color
        node.parent.color = Node.black
        if node_is_left_child:
            sibling.right.color = Node.black
            self.__rotate_left(node.parent)
        else:
            sibling.left.color = Node.black
            self.__rotate_right(node.parent)

    # -- Helpers for insertion and deletion --------------------------------------------------------- #
    
    def __rotate_left(self, node):
        parent = node.parent
        right_child = node.right

        node.right = right_child.left
        if right_child.left is not None:
            right_child.left.parent = node
        
        right_child.left = node
        node.parent = right_child

        self.__replace_parents_child(parent, node, right_child)

    def __rotate_right(self, node):
        parent = node.parent
        left_child = node.left

        node.left = left_child.right
        if left_child.right is not None:
            left_child.right.parent = node

        left_child.right = node 
        node.parent = left_child

        self.__replace_parents_child(parent, node, left_child)

    def __replace_parents_child(self, parent, old_child, new_child):
        if parent is None:
            self.root = new_child
        elif parent.left == old_child:
            parent.left = new_child
        elif parent.right == old_child:
            parent.right = new_child
        else:
            raise ValueError("The node is adopted!")
        
        if new_child is not None:
            new_child.parent = parent