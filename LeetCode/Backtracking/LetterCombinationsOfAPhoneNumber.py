# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. 
# Return the answer in any order.

# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

def letterCombinations(digits):
    letters = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z'],
    }
    res = []

    def backTrack(curr, i):
        if len(curr) == len(digits):
            res.append(''.join(curr))
            return 
        for comb in letters[digits[i]]:
            curr.append(comb)
            backTrack(curr, i + 1)
            curr.pop() 

    if digits:
        backTrack([], 0)

    return res

digits = "23"
# digits = ""
# digits = "2"

print(letterCombinations(digits))