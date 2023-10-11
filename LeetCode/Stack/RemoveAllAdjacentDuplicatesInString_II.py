# You are given a string s and an integer k, a k duplicate removal consists of choosing k adjacent and equal letters from s 
# and removing them, causing the left and the right side of the deleted substring to concatenate together.

# We repeatedly make k duplicate removals on s until we no longer can.

# Return the final string after all such duplicate removals have been made. It is guaranteed that the answer is unique.

def removeDuplicates(s, k):
    counter = []
    stack = []

    for i in range(len(s)):
        if not stack or stack[-1] != s[i]:
            counter.append(1)
        else:
            counter[-1] += 1
        stack.append(s[i])

        if counter[-1] == k:
            for _ in range(k):
                stack.pop()
            counter.pop()

    return "".join(stack)

s = "deeedbbcccbdaa"
k = 3
# aa

s = "pbbcggttciiippooaais"
k = 2
# ps

s = "abcd"
k = 2
# abcd

print(removeDuplicates(s, k))