# Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, 
# return the researcher's h-index.
# According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given 
# researcher has published at least h papers that have each been cited at least h times.

# Counting Sort

def hIndex(citations):
    n = len(citations)

    countArr = [0 for _ in range(n + 1)]

    for i in range(n):
        if citations[i] >= n:
            countArr[n] += 1
        else:
            countArr[citations[i]] += 1

    pos = 0

    for i in range(n + 1):
        while countArr[i] > 0:
            citations[pos] = i
            pos += 1
            countArr[i] -= 1

    h_index = 1

    for i in reversed(range(n)):
        if citations[i] >= h_index:
            h_index += 1
        else:
            return h_index - 1

    return n



# citations = [3,0,6,1,5]
# citations = [1,3,1]
# citations = [5,5,5,5,4]
citations = [0]

print(hIndex(citations))