# Given an array of integers citations where citations[i] is the number of citations a researcher received for their 
# ith paper and citations is sorted in ascending order, return the researcher's h-index.

# The h-index is defined as the maximum value of h such that the given researcher has published at least h papers 
# that have each been cited at least h times.

# You must write an algorithm that runs in logarithmic time.

def hIndex(citations):
    l, r = 0, len(citations) - 1
    h_index = 0
    while l <= r:
        mid = (l + r) // 2
        if citations[mid] == len(citations) - mid:
            return citations[mid]
        elif citations[mid] > len(citations) - mid:
            h_index = len(citations) - mid
            r = mid - 1
        else:
            l = mid + 1
    
    return h_index

citations = [0,1,3,5,6]

print(hIndex(citations))