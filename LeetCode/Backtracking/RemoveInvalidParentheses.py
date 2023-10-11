# Given a string s that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.

# Return a list of unique strings that are valid with the minimum number of removals. You may return the answer in any order.

def removeInvalidParentheses(s):
    left = right = 0

    for char in s:

        if char == '(':
            left += 1
        elif char == ')':
            # If we don't have a matching left, then this is a misplaced right, record it.
            if left == 0:
                right += 1
            else:
                left -= 1

    result = set()

    def backTrack(idx, left_count, right_count, remaining_lefts, remaining_rights, expr):
        if idx == len(s):
            if not remaining_lefts and not remaining_rights:
                result.add("".join(expr))
        else:
            # The discard case
            if (s[idx] == '(' and remaining_lefts > 0) or (s[idx] == ')' and remaining_rights > 0):
                backTrack(idx + 1,
                          left_count,
                          right_count,
                          remaining_lefts - (s[idx] == '('),
                          remaining_rights - (s[idx] == ')'),
                          expr)

            expr.append(s[idx])

            if s[idx] != '(' and s[idx] != ')':
                backTrack(idx + 1,
                          left_count,
                          right_count,
                          remaining_lefts,
                          remaining_rights,
                          expr)
            elif s[idx] == '(':
                backTrack(idx + 1,
                          left_count + 1,
                          right_count,
                          remaining_lefts,
                          remaining_rights,
                          expr)
            elif s[idx] == ')' and left_count > right_count:
                backTrack(idx + 1,
                          left_count,
                          right_count + 1,
                          remaining_lefts,
                          remaining_rights,
                          expr)
                
            expr.pop()

    backTrack(0, 0, 0, left, right, [])

    return list(result)


s = "()())()"
# s = "(a)())()"
# s = ")("

print(removeInvalidParentheses(s))