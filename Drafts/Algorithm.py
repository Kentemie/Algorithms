# Boyer-Moore Majority Voting Algorithm
# The Boyer-Moore voting algorithm is one of the popular optimal algorithms which is used to find the majority element among the 
# given elements that have more than N / 2 occurrences.

# def findMajority(arr):

#     votes, candidate = 0, None
#     for num in arr:
#         if votes == 0:
#             candidate = num
#             votes += 1
#         else:
#             if candidate == num:
#                 votes += 1
#             else:
#                 votes -= 1
#     if arr.count(candidate) > len(arr) // 2:
#         return candidate
#     else:
#         return -1
# nums = [1,1,1,2,3,5]
# majority = findMajority(nums)
# print(majority)





# Boyer Moore Algorithm for Pattern Searching: Bad Character Heuristic

# def badCharHeuristic(string):
#     badChar = [-1] * 256
#     for i in range(len(string)):
#         badChar[ord(string[i])] = i
#     return badChar

# def search(txt, pat):
#     m = len(pat)
#     n = len(txt)
#     s = 0
#     badChar = badCharHeuristic(pat)
#     while s <= n - m:
#         j = m - 1
#         while j >= 0 and pat[j] == txt[s + j]:
#             j -= 1
#         if j < 0:
#             print("Pattern occur at shift = {}".format(s))
#             s += (m - badChar[ord(txt[s + m])] if s + m < n else 1)
#         else:
#             s += max(1, j - badChar[ord(txt[s + j])])

# txt = "AABAACAADAABAABA"
# pat = "AABA" 
# search(txt, pat)





# Largest Sum Contiguous Subarray (Kadane’s Algorithm)
# Given an array arr[] of size N. The task is to find the sum of the contiguous subarray within a arr[] with the largest sum. 

# def maxSubArraySum(nums, n):
#     max_so_far = float("-inf")
#     max_ending_here = 0
#     start = 0
#     end = 0
#     j = 0
#     for i in range(n):
#         max_ending_here += nums[i]
#         if max_so_far < max_ending_here:
#             max_so_far = max_ending_here
#             start = j
#             end = i
#         if max_ending_here < 0:
#             max_ending_here = 0
#             j = i + 1
#     return(start, end, max_so_far)

# nums = [-2, -3, 4, -1, -2, 1, 5, -3]
# print(maxSubArraySum(nums, len(nums)))





# Bits list to integer 

# def intcaststr(bitlist):
#     return int("".join(str(i) for i in bitlist), 2)

# def intcastlookup(bitlist):
#     return int(''.join('01'[i] for i in bitlist), 2)

# def shifting(bitlist):
#     out = 0
#     for bit in bitlist:
#       out = (out << 1) | bit
#     return out

# timeit.timeit('convert([1,0,0,0,0,0,0,0])', 'from __main__ import intcaststr as convert', number=100000)
# 0.5659139156341553
# timeit.timeit('convert([1,0,0,0,0,0,0,0])', 'from __main__ import intcastlookup as convert', number=100000)
# 0.4642159938812256
# timeit.timeit('convert([1,0,0,0,0,0,0,0])', 'from __main__ import shifting as convert', number=100000)
# 0.1406559944152832





# Lomuto’s Partition Scheme O(N2); O(1) 

# def partition(arr, low, high):
#     pivot = arr[high]
#     j = low - 1
#     for i in range(low, high):
#         if arr[i] <= pivot:
#             j += 1
#             arr[j], arr[i] = arr[i], arr[j]
#     arr[j + 1], arr[high] = arr[high], arr[j + 1]
#     return j + 1 
   
# def quickSort(arr, low, high):
#     if low < high:
#         pi = partition(arr, low, high)
#         quickSort(arr, low, pi - 1)
#         quickSort(arr, pi + 1, high)

# arr = [10, 7, 8, 9, 1, 5]
# quickSort(arr, 0, len(arr) - 1)
# print(arr)


# Hoare’s Partition Scheme  O(N); O(1)

# def partition(arr, low, high):
#     pivot = arr[low]
#     i = low - 1
#     j = high + 1
#     while True:
#         i += 1
#         while arr[i] < pivot:
#             i += 1
#         j -= 1
#         while arr[j] > pivot:
#             j -= 1
#         if i >= j:
#             return j
#         arr[i], arr[j] = arr[j], arr[i]

# def quickSort(arr, low, high):
#     if low < high:
#         pi = partition(arr, low, high)
#         quickSort(arr, low, pi)
#         quickSort(arr, pi + 1, high)

# arr = [10, 7, 8, 9, 1, 5]
# quickSort(arr, 0, len(arr) - 1)
# print(arr)


# Quickselect Algorithm O(n), with a worst-case of O(n^2)

# Quickselect is a selection algorithm to find the k-th smallest element in an unordered list. 
# It is related to the quick sort sorting algorithm.

# def partition(arr, low, high):
#     pivot = arr[high]
#     j = low
#     for i in range(low, high):
#         if arr[i] <= pivot:
#             arr[j], arr[i] = arr[i], arr[j]
#             j += 1
#     arr[j], arr[high] = arr[high], arr[j]
#     return j

# def kthSmallest(arr, low, high, k):
#     if k > 0 and k <= high - low + 1:
#         pi = partition(arr, low, high)
#         if pi - low == k - 1:
#             return arr[pi]
#         if pi - low > k - 1:
#             return kthSmallest(arr, low, pi - 1, k)
#         return kthSmallest(arr, pi + 1, high, k - pi + low - 1)
#     print("Index out of bound")

# arr = [10, 4, 5, 8, 6, 11, 26]
# n = len(arr)
# k = 1

# print(kthSmallest(arr, 0, n - 1, k))





# Counting Sort 

# O(n); O(n)

# def countSort(arr):
#     minElem = min(arr)
#     maxElem = max(arr)
#     rangeOfElem = maxElem - minElem + 1
#     countArr = [0 for _ in range(rangeOfElem)]
#     outputArr = [0 for _ in range(len(arr))]
#     for i in range(len(arr)):
#         countArr[arr[i] - minElem] += 1
#     for i in range(1, len(countArr)):
#         countArr[i] += countArr[i - 1]
#     for i in range(len(arr) - 1, -1, -1):
#         outputArr[countArr[arr[i] - minElem] - 1] = arr[i]
#         countArr[arr[i] - minElem] += 1
#     return outputArr

# arr = [-5, -10, 0, -3, 8, 5, -1, 10]
# print(countSort(arr))


# O(N + K); O(N + K)

# def countSort(ss):
#     outputArr = [0 for _ in range(len(ss))]
#     countArr = [0 for _ in range(256)]
#     for i in ss:
#         countArr[ord(i)] += 1
#     for i in range(1, 256):
#         countArr[i] += countArr[i - 1]
#     for i in range(len(ss)):
#         outputArr[countArr[ord(ss[i])] - 1] = ss[i]
#         countArr[ord(ss[i])] -= 1
#     return outputArr

# ss = "geeksforgeeks"
# print("".join(countSort(ss)))





# Least Significant Digit (LSD) Radix Sort O(N*M) where M = length of the longest string; O(N + B)

# A problem we encounter with counting sort is that it can’t easily handle strings where the alphabet size could be unconstrained. 
# Additionally, when the maximum value of the array is extraordinarily large, counting sort will lose its appeal since the additional memory 
# overhead can cause things to slow down quite a bit.
# Radix sort is an extension of counting sort that handles these problems. 
# It works well with collections of strings and collections of integers (especially when the maximum value is large).

# def countSort(nums: list[int], place_val: int, K: int = 10) -> None:
#     countArr = [0] * K
#     for num in nums:
#         digit = (num // place_val) % 10
#         countArr[digit] += 1
#     starting_index = 0
#     for i, count in enumerate(countArr):
#         countArr[i] = starting_index
#         starting_index += count  
#     outputArr = [0] * len(nums)
#     for num in nums:
#         digit = (num // place_val) % 10
#         outputArr[countArr[digit]] = num
#         countArr[digit] += 1
#     for i in range(len(outputArr)):
#         nums[i] = outputArr[i]

# def radixSort(nums: list[int]) -> None:

#     minElem = min(nums)
#     nums[:] = [num - minElem for num in nums]
#     maxElem = max(nums)
#     place_val = 1
#     while place_val <= maxElem:
#         countSort(nums, place_val)
#         place_val *= 10
#     nums[:] = [num + minElem for num in nums]

# nums = [9415, 5908, 1840, 5907]
# radixSort(nums)
# print(nums)





# Floyd's Cycle-Finding Algorithm
# This algorithm is based on 2 runners running around a circular race track, a fast runner and a slow runner. 
# In reference to a famous fable, many people call the slow runner the "tortoise" and the fast runner the "hare".
# Regardless of where the tortoise and hare start in the cycle, they are guaranteed to eventually meet. 
# This is because the hare moves one node closer to the tortoise (in their direction of movement) each step.

# def isHappy(n: int) -> bool: 
#     def getNext(n):
#         totalSum = 0
#         while n > 0:
#             n, digit = divmod(n, 10)
#             totalSum += digit ** 2
#         return totalSum
#     tortoise = n
#     hare = getNext(n)
#     while hare != 1 and tortoise != hare:
#         tortoise = getNext(tortoise)
#         hare = getNext(getNext(hare))
#     return hare == 1

# n = 2
# print(isHappy(n))





# Insertion Sort O(n^2); O(1)
# For small inputs, insertion sort almost always outperforms other sorts. Also when the number of inversions is small (the list is almost sorted), 
# insertion sort is quite efficient, since there aren't many insertion operations required.
# It is a stable sorting algorithm since equal elements will never have swapped places, so their relative ordering will be preserved.

# def insertionSort(nums):
#     for i in range(1, len(nums)):
#         curr = i
#         while curr > 0 and nums[curr - 1] > nums[curr]:
#             nums[curr], nums[curr - 1] = nums[curr - 1], nums[curr]
#             curr -= 1
# nums = [7,3,2,5,6,10,9,8,1]
# insertionSort(nums)
# print(nums)
