# Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is 
# the smallest in lexicographical order among all possible results.


def removeDuplicateLetters(s):
    last_occurance = { char: idx for idx, char in enumerate(s) }
    seen = set()
    stack = []

    for idx, char in enumerate(s):
        if char not in seen:
            while stack and char < stack[-1] and idx < last_occurance[stack[-1]]:
                seen.discard(stack.pop())

            seen.add(char)
            stack.append(char)
    
    return "".join(stack)


s = "cbacdcbc"

print(removeDuplicateLetters(s))