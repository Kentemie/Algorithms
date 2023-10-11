# The AVL tree and other self-balancing search trees like Red Black are useful to get all basic operations done in O(log n) 
# time. The AVL trees are more balanced compared to Red-Black Trees, but they may cause more rotations during insertion and 
# deletion. So if your application involves many frequent insertions and deletions, then Red Black trees should be preferred.
# And if the insertions and deletions are less frequent and search is the more frequent operation, then the AVL tree should 
# be preferred over Red Black Tree.

class TreeNode:
    def __init__(self, val=0, left=None, right=None, height=1):
        self.val = val
        self.left = left
        self.right = right
        self.height = height

class AVL_Tree:
    def insert(self, root, val):

        # Step 1 - Perform normal BST
        if not root:
            return TreeNode(val)
        if val < root.val:
            root.left = self.insert(root.left, val)
        else:
            root.right = self.insert(root.right, val)

        # Step 2 - Update the height of the
        # ancestor node
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        # Step 3 - Get the balance factor
        BF = self.getBalance(root)

        # Step 4 - If the node is unbalanced,
        # then try out the 4 cases
        # Case 1 - Left Left
        #               T1, T2, T3 and T4 are subtrees.
        #          z                                      y 
        #         / \                                   /   \
        #        y   T4      Right Rotate (z)          x      z
        #       / \          - - - - - - - - ->      /  \    /  \ 
        #      x   T3                               T1  T2  T3  T4
        #     / \
        #   T1   T2
        if BF > 1 and val < root.left.val:
            return self.rightRotate(root)
        
        # Case 2 - Right Right
        #     z                                y
        #    /  \                            /   \ 
        #   T1   y     Left Rotate(z)       z      x
        #       /  \   - - - - - - - ->    / \    / \
        #      T2   x                     T1  T2 T3  T4
        #          / \
        #        T3  T4
        if BF < -1 and val > root.right.val:
            return self.leftRotate(root)
        
        # Case 3 - Left Right
        #       z                               z                           x
        #      / \                            /   \                        /  \ 
        #     y   T4  Left Rotate (y)        x    T4  Right Rotate(z)    y      z
        #    / \      - - - - - - - - ->    /  \      - - - - - - - ->  / \    / \
        #  T1   x                          y    T3                    T1  T2 T3  T4
        #      / \                        / \
        #    T2   T3                    T1   T2
        if BF > 1 and val > root.left.val:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        
        # Case 4 - Right Left
        #      z                            z                            x
        #     / \                          / \                          /  \ 
        #   T1   y   Right Rotate (y)    T1   x      Left Rotate(z)   z      y
        #       / \  - - - - - - - - ->     /  \   - - - - - - - ->  / \    / \
        #      x   T4                      T2   y                  T1  T2  T3  T4
        #     / \                              /  \
        #   T2   T3                           T3   T4
        if BF < -1 and val < root.right.val:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
        
        return root
    
    def delete(self, root, val):

        # Step 1 - Perform standard BST delete
        if not root:
            return None
        
        elif val < root.val:
            root.left = self.delete(root.left, val)

        elif val > root.val:
            root.right = self.delete(root.right, val)

        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            
            temp = self.getMinValueNode(root.right)
            root.val = temp.val
            root.right = self.delete(root.right, temp.val)
        
        if root is None:
            return None
        
        # Step 2 - Update the height of the
        # ancestor node
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        # Step 3 - Get the balance factor
        BF = self.getBalance(root)

        # Step 4 - If the node is unbalanced,
        # then try out the 4 cases
        # Case 1 - Left Left
        #               T1, T2, T3 and T4 are subtrees.
        #          z                                      y 
        #         / \                                   /   \
        #        y   T4      Right Rotate (z)          x      z
        #       / \          - - - - - - - - ->      /  \    /  \ 
        #      x   T3                               T1  T2  T3  T4
        #     / \
        #   T1   T2
        if BF > 1 and self.getBalance(root.left) >= 0:
            return self.rightRotate(root)
        
        # Case 2 - Right Right
        #     z                                y
        #    /  \                            /   \ 
        #   T1   y     Left Rotate(z)       z      x
        #       /  \   - - - - - - - ->    / \    / \
        #      T2   x                     T1  T2 T3  T4
        #          / \
        #        T3  T4
        if BF < -1 and self.getBalance(root.right) <= 0:
            return self.leftRotate(root)
        
        # Case 3 - Left Right
        #       z                               z                           x
        #      / \                            /   \                        /  \ 
        #     y   T4  Left Rotate (y)        x    T4  Right Rotate(z)    y      z
        #    / \      - - - - - - - - ->    /  \      - - - - - - - ->  / \    / \
        #  T1   x                          y    T3                    T1  T2 T3  T4
        #      / \                        / \
        #    T2   T3                    T1   T2
        if BF > 1 and self.getBalance(root.left) < 0:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        
        # Case 4 - Right Left
        #      z                            z                            x
        #     / \                          / \                          /  \ 
        #   T1   y   Right Rotate (y)    T1   x      Left Rotate(z)   z      y
        #       / \  - - - - - - - - ->     /  \   - - - - - - - ->  / \    / \
        #      x   T4                      T2   y                  T1  T2  T3  T4
        #     / \                              /  \
        #   T2   T3                           T3   T4
        if BF < -1 and self.getBalance(root.right) > 0:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
        
        return root
        
    def getHeight(self, root):
        if not root:
            return 0
        return root.height
    
    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)
    
    def rightRotate(self, z):
        y = z.left
        T3 = y.right
        
        # Perform rotation
        y.right = z
        z.left = T3

        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y
    
    def leftRotate(self, z):
        y = z.right
        T2 = y.left

        # Perform rotation
        y.left = z
        z.right = T2

        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y
    
    def getMinValueNode(self, root):
        if not root or not root.left:
            return root
        return self.getMinValueNode(root.left)
    
    def preOrder(self, root):
        if not root:
            return 
        print(root.val, end=" ")
        self.preOrder(root.left)
        self.preOrder(root.right)

avl = AVL_Tree()
root = None
nums = [9, 5, 10, 0, 6, 11, -1, 1, 2]

for num in nums:
    root = avl.insert(root, num)

# root = avl.insert(root, 10)
# root = avl.insert(root, 20)
# root = avl.insert(root, 30)
# root = avl.insert(root, 40)
# root = avl.insert(root, 50)
# root = avl.insert(root, 25)

avl.preOrder(root)
print()

root = avl.delete(root, 10)

avl.preOrder(root)