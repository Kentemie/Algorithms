# Design a text editor with a cursor that can do the following:

    # Add text to where the cursor is.
    # Delete text from where the cursor is (simulating the backspace key).
    # Move the cursor either left or right.

# When deleting text, only characters to the left of the cursor will be deleted. The cursor will also remain within the actual text 
# and cannot be moved beyond it. More formally, we have that 0 <= cursor.position <= currentText.length always holds.

# Implement the TextEditor class:

    # TextEditor() Initializes the object with empty text.
    # void addText(string text) Appends text to where the cursor is. The cursor ends to the right of text.
    # int deleteText(int k) Deletes k characters to the left of the cursor. Returns the number of characters actually deleted.
    # string cursorLeft(int k) Moves the cursor to the left k times. Returns the last min(10, len) characters to the left of the 
    # cursor, where len is the number of characters to the left of the cursor.
    # string cursorRight(int k) Moves the cursor to the right k times. Returns the last min(10, len) characters to the left of the
    # cursor, where len is the number of characters to the left of the cursor.

# Approach 1: Doubly Linked List

# class Node:

#     def __init__(self, char = "", next = None, prev = None):
#         self.char = char 
#         self.next = next
#         self.prev = prev


# class TextEditor:

#     def __init__(self):
#         self.cursor = Node("|")
#         self.head = Node("#")
#         self.tail = Node("#")
#         self.left_length = 0
#         self.right_length = 0

#         self.cursor.prev = self.head
#         self.head.next = self.cursor
#         self.cursor.next = self.tail
#         self.tail.prev = self.cursor

#     def addText(self, text: str) -> None:
#         for char in text:
#             node = Node(char)
#             prev_node = self.cursor.prev
#             prev_node.next = node
#             node.prev = prev_node
#             node.next = self.cursor
#             self.cursor.prev = node

#             self.left_length += 1

#     def deleteText(self, k: int) -> int:
#         dummy = self.cursor
#         actual_removal_amount = min(self.left_length, k)
        
#         for _ in range(actual_removal_amount):
#             dummy = dummy.prev
        
#         self.cursor.prev = dummy.prev
#         dummy.prev.next = self.cursor
#         self.left_length -= actual_removal_amount

#         return actual_removal_amount

#     def cursorLeft(self, k: int) -> str:
#         string_builder = []
#         actual_number_of_moves = min(self.left_length, k)
#         if actual_number_of_moves:
#             dummy = self.cursor

#             for _ in range(actual_number_of_moves):
#                 dummy = dummy.prev

#             self.cursor.prev.next = self.cursor.next
#             self.cursor.next.prev = self.cursor.prev

#             dummy.prev.next = self.cursor
#             self.cursor.prev = dummy.prev
#             dummy.prev = self.cursor
#             self.cursor.next = dummy

#             self.left_length -= actual_number_of_moves
#             self.right_length += actual_number_of_moves
        
#         dummy = self.cursor
        
#         for _ in range(min(self.left_length, 10)):
#             dummy = dummy.prev
#             string_builder.append(dummy.char)

#         return "".join(string_builder[::-1])

#     def cursorRight(self, k: int) -> str:
#         string_builder = []
#         actual_number_of_moves = min(self.right_length, k)
#         if actual_number_of_moves:
#             dummy = self.cursor

#             for _ in range(actual_number_of_moves):
#                 dummy = dummy.next

#             self.cursor.prev.next = self.cursor.next
#             self.cursor.next.prev = self.cursor.prev

#             dummy.next.prev = self.cursor
#             self.cursor.next = dummy.next
#             dummy.next = self.cursor
#             self.cursor.prev = dummy

#             self.left_length += actual_number_of_moves
#             self.right_length -= actual_number_of_moves
        
#         dummy = self.cursor
        
#         for _ in range(min(self.left_length, 10)):
#             dummy = dummy.prev
#             string_builder.append(dummy.char)

#         return "".join(string_builder[::-1])


# textEditor = TextEditor()
# head = textEditor.head
# tail = textEditor.tail
# textEditor.addText("leetcode")
# print(textEditor.deleteText(4))
# textEditor.addText("practice")
# print(textEditor.cursorRight(3))
# print(textEditor.cursorLeft(8))
# print(textEditor.deleteText(10))
# print(textEditor.cursorLeft(2))
# print(textEditor.cursorRight(6))

# ----------------------------------------------------------------------------------------------------------------------------- #

# Approach 2: Deque

from collections import deque

class TextEditor:
    
    def __init__(self):
        self.left = []
        self.right = deque([])

    def addText(self, text: str) -> None:
        for char in text:
            self.left.append(char)
    
    def deleteText(self, k: int) -> int:
        actual_removal_amount = min(len(self.left), k)

        for _ in range(actual_removal_amount):
            self.left.pop()

        return actual_removal_amount
    
    def cursorLeft(self, k: int) -> str:
        actual_number_of_moves = min(len(self.left), k)

        for _ in range(actual_number_of_moves):
            self.right.appendleft(self.left.pop())
        
        if len(self.left) < 10:
            return "".join(self.left)
        return "".join(self.left[len(self.left) - 10:])

    def cursorRight(self, k: int) -> str:
        actual_number_of_moves = min(len(self.right), k)

        for _ in range(actual_number_of_moves):
            self.left.append(self.right.popleft())
        
        if len(self.left) < 10:
            return "".join(self.left)
        return "".join(self.left[len(self.left) - 10:])


textEditor = TextEditor()

textEditor.addText("leetcode")
print(textEditor.deleteText(4))
textEditor.addText("practice")
print(textEditor.cursorRight(3))
print(textEditor.cursorLeft(8))
print(textEditor.deleteText(10))
print(textEditor.cursorLeft(2))
print(textEditor.cursorRight(6))