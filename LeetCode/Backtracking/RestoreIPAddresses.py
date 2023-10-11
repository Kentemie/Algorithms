# A valid IP address consists of exactly four integers separated by single dots. Each integer is between 0 and 255 (inclusive) 
# and cannot have leading zeros.

    # For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011.255.245", "192.168.1.312" and "192.168@1.1" are 
    # invalid IP addresses.

# Given a string s containing only digits, return all possible valid IP addresses that can be formed by inserting dots into s. 
# You are not allowed to reorder or remove any digits in s. You may return the valid IP addresses in any order.

def restoreIpAddresses(s):
    res = []

    def backTrack(curr, start, dotCnt, length):
        if dotCnt == 4 and length == len(s):
            res.append(list(curr))
            return
        for end in range(start, len(s)):
            if 0 <= int(s[start : end + 1]) <= 255:
                if (end - start + 1) > 1 and s[start] == '0':
                    continue
                curr.append(s[start : end + 1])
                backTrack(curr, end + 1, dotCnt + 1, length + (end - start + 1))
                curr.pop()
    
    backTrack([], 0, 0, 0)

    for i in range(len(res)):
        res[i] = '.'.join(res[i])

    return res

s = "25525511135"
s = "0000"
s = "101023"

print(restoreIpAddresses(s))