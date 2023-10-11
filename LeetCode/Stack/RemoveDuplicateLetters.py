# Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is 
# the smallest in lexicographical order among all possible results.

def removeDuplicateLetters(s):
    seen = set()
    indices = {char: i for i, char in enumerate(s)}
    stack = []

    for i, char in enumerate(s):
        if char not in seen:
            while stack and char < stack[-1] and i < indices[stack[-1]]:
                seen.discard(stack.pop())
            stack.append(char)
            seen.add(char)

    return "".join(stack)

s = "bcabc"
# "abc"

s = "cbacdcbc"
# "acdb"

print(removeDuplicateLetters(s))