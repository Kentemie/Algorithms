# Given an encoded string, return its decoded string.

# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly 
# k times. Note that k is guaranteed to be a positive integer.

# You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, 
# etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those 
# repeat numbers, k. For example, there will not be input like 3a or 2[4].

# The test cases are generated so that the length of the output will never exceed 105.

def decodeString(s):
    stack = []
    for char in s:
        if char == ']':
            stringBuilder = []
            
            while stack[-1] != '[':
                stringBuilder.append(stack.pop())

            stack.pop()
            cnt = 0
            base = 1
            
            while stack and stack[-1].isdigit():
                cnt += base * int(stack.pop())
                base *= 10
            
            while cnt != 0:
                for ch in reversed(stringBuilder):
                    stack.append(ch)
                cnt -= 1
        else:
            stack.append(char)
    return "".join(stack)


s = "3[a]2[bc]"
# "aaabcbc"
s = "3[a2[c]]"
# "accaccacc"
s = "2[abc]3[cd]ef"
# "abcabccdcdcdef"

print(decodeString(s))