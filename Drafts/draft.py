# Given a string s and a character c that occurs in s, return an array of integers answer where answer.length == s.length 
# and answer[i] is the distance from index i to the closest occurrence of character c in s.
# The distance between two indices i and j is abs(i - j), where abs is the absolute value function.

# s = "loveleetcode"
# c = "e"
# res = []
# prev = float('-inf')
# for i in range(len(s)):
#     if s[i] == c:
#         prev = i
#     res.append(i - prev)
# prev = float('inf')
# for i in range(len(s) - 1, -1, -1):
#     if s[i] == c:
#         prev = i
#     res[i] = min(res[i], prev - i)
# print(res)




# Two strings are similar if they consist of the same characters.

# For example, "abca" and "cba" are similar since both consist of characters 'a', 'b', and 'c'.
# However, "abacba" and "bcfd" are not similar since they do not consist of the same characters.
# words = ["aba","aabb","abcd","bac","aabc"]
# d = {}
# for word in words:
#     bit = 0
#     for char in word:
#         bit |= 1 << (ord(char) - ord('a'))
#     if bit not in d:
#         d[bit] = 1
#     else:
#         d[bit] += 1
# pairs = 0
# for item, val in d.items():
#     pairs += (val - 1) * val // 2
# print(pairs)




# Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is 
# the number of times it appears in the string.
# Approach 1: Arrays and Sorting O(nlogn); O(n)

# s = "tree"
# s = list(s)
# s.sort()
# all_strings = []
# cur_strbuild = [s[0]]
# for ch in s[1:]:
#     if cur_strbuild[-1] != ch:
#         all_strings.append("".join(cur_strbuild))
#         cur_strbuild = []
#     cur_strbuild.append(ch)
# all_strings.append("".join(cur_strbuild))
# all_strings.sort(key = lambda string: len(string), reverse = True)
# new_s = "".join(all_strings)
# print(new_s)


# Approach 2: HashMap and Sort O(nlog⁡n) OR O(n + klog⁡k); O(n)

# from collections import Counter
# count = Counter(s)
# string_builder = []
# for char, freq in count.most_common():
#     string_builder.append(char * freq)
# new_s = "".join(string_builder)
# print(new_s)


# Approach 3: Multiset and Bucket Sort O(n); O(n)
# Recall that Bucket Sort is the sorting algorithm where items are placed at Array indexes based on their values 
# (the indexes are called "buckets"). For this problem, we'll need to have a List of characters at each index. 

# from collections import Counter
# count = Counter(s)
# max_freq = max(count.values())
# buckets = [[] for _ in range(max_freq + 1)]
# for ch, i in count.items():
#     buckets[i].append(ch)
# string_builder = []
# for i in range(len(buckets) - 1, 0, -1):
#     for ch in buckets[i]:
#         string_builder.append(ch * i)
# new_s = "".join(string_builder)
# print(new_s)




# Top K Frequent Words
# Given an array of strings words and an integer k, return the k most frequent strings.
# Return the answer sorted by the frequency from highest to lowest. 
# Sort the words with the same frequency by their lexicographical order.

# Approach 1: Max Heap O(N+klogN); O(N)
# from collections import Counter 
# from heapq import heapify, heappop
# words = ["i","love","leetcode","i","love","coding","a","b"]
# k = 3
# cnt = Counter(words)
# heap = [(-freq, word) for word, freq in cnt.items()]
# heapify(heap)
# print(heap)
# ans = [heappop(heap)[1] for _ in range(k)]
# print(ans)

# Approach 2: Min Heap O(Nlogk); O(N)
# from collections import Counter
# from heapq import heappush, heappop
# class Pair:
#     def __init__(self, word, freq):
#         self.word = word
#         self.freq = freq
#     def __lt__(self, p):
#         return self.freq < p.freq or (self.freq == p.freq and self.word > p.word)

# words = ["i","love","leetcode","i","love","coding"]
# k = 3
# cnt = Counter(words)
# heap = []
# for word, freq in cnt.items():
#     heappush(heap, Pair(word, freq))
#     if len(heap) > k:
#         heappop(heap)
# ans = [p.word for p in sorted(heap, reverse = True)]
# print(ans)    




# Find Common Characters
# Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). 
# You may return the answer in any order.

# from collections import Counter
# from functools import reduce
# words = ["bella","label","roller"]
# print(list(reduce(Counter.__and__, map(Counter, words)).elements()))




# Binary Gap
# Given a positive integer n, find and return the longest distance between any two adjacent 1's in the binary representation of n. 
# If there are no two adjacent 1's, return 0.
# Two 1's are adjacent if there are only 0's separating them (possibly no 0's). 
# The distance between two 1's is the absolute difference between their bit positions. For example, the two 1's in "1001" have a distance of 3.
# n = 22
# last = None
# ans = 0
# for i in range(32):
#     if (n >> i) & 1:
#         if last is not None:
#             ans = max(ans, i - last)
#         last = i
# print(i, last, ans)




# Third Maximum Number
# Given an integer array nums, return the third distinct maximum number in this array. 
# If the third maximum does not exist, return the maximum number.


# Min Heap and Set
# from heapq import heappop, heappush
# nums = [3,2,2,1]
# heap = []
# seen = set()
# for num in nums:
#     if num in seen:
#         continue
#     if len(heap) == 3:
#         if heap[0] < num:
#             seen.remove(heap[0])
#             heappop(heap)

#             heappush(heap, num)
#             seen.add(num)
#     else:
#         heappush(heap, num)
#         seen.add(num)
# if len(heap) == 1:
#     print(heap[0])
# elif len(heap) == 2:
#     first = heappop(heap)
#     print(max(first, heappop(heap)))
# else:
#     print(heap[0])


# OrderedSet
# from sortedcontainers import SortedSet   
# sorted_nums = SortedSet()
# for num in nums:
#     if num in sorted_nums:
#         continue
#     if len(sorted_nums) == 3:
#         if sorted_nums[0] < num:
#             sorted_nums.discard(sorted_nums[0])
#             sorted_nums.add(num)
#     else:
#         sorted_nums.add(num)
# if len(sorted_nums) == 3:
#     print(sorted_nums[0])
# else:
#     print(sorted_nums[-1])


# 3 Pointers
# first_max, second_max, third_max = float('-inf'), float('-inf'), float('-inf')
# for num in nums:
#     if first_max == num or second_max == num or third_max == num:
#         continue
#     if first_max < num:
#         third_max = second_max
#         second_max = first_max
#         first_max = num
#     elif second_max < num:
#         third_max = second_max
#         second_max = num
#     elif third_max < num:
#         third_max = num
# if third_max == float('-inf'):
#     print(first_max)
# else:
#     print(third_max)




# Tasks.py #2 TLE

# from functools import cmp_to_key
# nums = ["3","6","7","10"]
# k = 4
# def sorter(x, y):
#     n, m = len(x), len(y)
#     if n != m:
#         return -1 if n < m else 1
#     else:
#         return -1 if x < y else 1

# key = cmp_to_key(sorter)
# nums.sort(key = key, reverse = True)
# print(nums[k - 1])




# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, 
# with the colors in the order red, white, and blue.
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

# The problem is known as Dutch National Flag Problem and first was proposed by Edsger W. Dijkstra. 

# nums = [2,0,2,1,1,0]

# p0, curr = 0, 0
# p2 = len(nums) - 1

# while curr <= p2:
#     if nums[curr] == 0:
#         nums[p0], nums[curr] = nums[curr], nums[p0]
#         curr += 1
#         p0 += 1
#     elif nums[curr] == 2:
#         nums[curr], nums[p2] = nums[p2], nums[curr]
#         p2 -= 1
#     else:
#         curr += 1

# print(nums)




# Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements.
# Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows
# a, b are from arr
# a < b
# b - a equals to the minimum absolute difference of any two elements in arr.

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
#     return outputArr
    
# arr = [1,3,6,10,15]
# res = []
# arr2 = countSort(arr)
# minDiff = float("inf")
# for i in range(len(arr2) - 1):
#     currDiff = arr2[i + 1] - arr2[i]
#     if currDiff == minDiff:
#         res.append([arr2[i], arr2[i + 1]])
#     elif currDiff < minDiff:
#         res = [[arr2[i], arr2[i + 1]]]
#         minDiff = currDiff
# print(res)




# Tasks.py #3
# TLE

# def countSort(nums: list[str], pos: int) -> None:
#     countArr = [0 for _ in range(58)]
#     outputArr = ["" for _ in range(len(nums))]
#     for num in nums:
#         countArr[ord(num[pos])] += 1
#     starting_index = 0
#     for i, cnt in enumerate(countArr):
#         countArr[i] = starting_index
#         starting_index += cnt 
#     for num in nums:
#         outputArr[countArr[ord(num[pos])]] = num
#         countArr[ord(num[pos])] += 1   
#     for i in range(len(nums)):
#         nums[i] = outputArr[i]

# def radixSort(nums: list[str], indexArr: list[str], trim: int, kthMin: int) -> int:
#     pos = len(nums[0]) - 1
#     for _ in range(trim - 1, -1, -1):     
#         countSort(nums, pos)
#         pos -= 1
#     cnt = 0
#     minPos = 0
#     for i in range(len(indexArr)):
#         if indexArr[i] == nums[kthMin - 1]:
#             cnt += 1
#             minPos = i
#         if cnt > 1:
#             if cnt == kthMin:
#                 minPos = i
#     return minPos

# nums = ["9415","5908","1840","5307"]

# queries = [[3,2],[2,2],[3,3],[1,3]]
# indexArr = []
# for num in nums:
#     indexArr.append(num)
# res = []
# for i in range(len(queries)):
#     res.append(radixSort(nums, indexArr, queries[i][1], queries[i][0]))
#     nums[:] = indexArr

# print(res)

# AC, but not required solution

# nums = ["9415","5908","1840","5307"]
# queries = [[3,2],[2,2],[3,3],[1,3]]
# ans, trimmed = [], {}
# for k, trim in queries:
#     trimmed.setdefault(trim, sorted([(num[-trim:], i) for i, num in enumerate(nums)]))
#     ans.append(trimmed[trim][k - 1][1])
# print(ans)




# Add Binary
# Given two binary strings a and b, return their sum as a binary string.

# def add_binary_string(a, b):
#     i, j = len(a) - 1, len(b) - 1
#     res = ""
#     carry = 0
#     while i >= 0 or j >= 0:
#         sum_ = carry
#         if i >= 0:
#             sum_ += int(a[i])
#             i -= 1
#         if j >= 0:
#             sum_ += int(b[j])
#             j -= 1
#         res = str(sum_ % 2) + res
#         carry = sum_ // 2
#     if carry > 0:
#         res = '1' + res
#     return res 
# a = "11"
# b = "1"
# print(add_binary_string(a, b))




# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# def badCharacter(pat):
#     badChar = [-1] * 256
#     for i in range(len(pat)):
#         badChar[ord(pat[i])] = i
#     return badChar

# def search(txt, pat):
#     n, m = len(txt), len(pat)
#     shift = 0
#     badChar = badCharacter(pat)
#     while shift <= n - m:
#         j = m - 1
#         while j >= 0 and pat[j] == txt[shift + j]:
#             j -= 1
#         if j < 0:
#             return shift
#         else: 
#             shift += max(1, j - badChar[ord(txt[shift + j])])
#     return -1

# haystack = "sadbutsad"
# needle = "sad"
# print(search(haystack, needle))




# Longest Common Prefix
# Write a function to find the longest common prefix string amongst an array of strings.

# def longest_common_prefix(strs):
#     if not strs:
#         return ""
#     prefix = strs[0]
#     for st in strs:
#         while not st.startswith(prefix):
#             prefix = prefix[:-1]
#             if not prefix:
#                 return ""
#     return prefix


# strs = ["flower","flow","flight"]
# print(longest_common_prefix(strs))


# def LCP(strs, left, right):
#     if left == right:
#         return strs[left]
#     else:
#         mid = (left + right) // 2
#         lcpLeft = LCP(strs, left, mid)
#         lcpRight = LCP(strs, mid + 1, right)
#         print(lcpLeft, lcpRight)
#         print(commonPrefix(lcpLeft, lcpRight))
#         return commonPrefix(lcpLeft, lcpRight)

# def commonPrefix(left, right):
#     minLen = min(len(left), len(right))
#     for i in range(minLen):
#         if left[i] != right[i]:
#             return left[:i]
#     return left[:minLen]

# strs = ["leetcode","leet","lee","le"]
# LCP(strs, 0, len(strs) - 1)




# Array Partition I
# Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn) 
# such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum.

# def countSort(arr):
#     maxElem = max(arr)
#     minElem = min(arr)
#     rangeOfElem = maxElem - minElem + 1
#     countArr = [0] * rangeOfElem
#     maxSum = 0
#     isEvenIndex = True
#     for num in arr:
#         countArr[num - minElem] += 1
#     for i in range(rangeOfElem):
#         while countArr[i] > 0:
#             if isEvenIndex:
#                 maxSum += i + minElem
#             isEvenIndex = not isEvenIndex
#             countArr[i] -= 1
#     return maxSum

# nums = [6,2,6,5,1,2]
# print(countSort(nums))




# Happy Number
# A happy number is a number defined by the following process:

# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.

# def getNumber(n):
#     totalSum = 0
#     while n > 0:
#         n, digit = divmod(n, 10)
#         totalSum += digit ** 2
#     return totalSum

# seen = set()
# n = 19

# while n != 1 and n not in seen:
#     seen.add(n)
#     n = getNumber(n)
# print(n)




# Group Shifted Strings
# We can shift a string by shifting each of its letters to its successive letter.
# For example, "abc" can be shifted to be "bcd".
# We can keep shifting the string to form a sequence.
# For example, we can keep shifting "abc" to form the sequence: "abc" -> "bcd" -> ... -> "xyz".

# from collections import defaultdict
# def shiftLetter(letter, shift):
#     return chr((ord(letter) - shift) % 26 + ord('a'))

# def getHash(ss):
#     shift = ord(ss[0])
#     return ''.join(shiftLetter(letter, shift) for letter in ss)

# strings = ["abc","bcd","acef","xyz","az","ba","a","z"]

# d = defaultdict(list)
# for ss in strings:
#     key = getHash(ss)
#     d[key].append(ss)

# print(d.values())




# Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without repeating characters.

# from collections import Counter
# s = "abcabcbb"
# ch = Counter()
# left, right = 0, 0
# res = 0
# while right < len(s):
#     ch[s[right]] += 1
#     while ch[s[right]] > 1:
#         ch[s[left]] -= 1
#         left += 1
#     res = max(res, right - left + 1)
#     right += 1
# print(res)




# 3Sum
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, 
# and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

# def countSort(nums):
#     maxElem = max(nums)
#     minElem = min(nums)
#     maxRange = maxElem - minElem + 1
#     countArr = [0] * maxRange
#     outputArr = [0] * len(nums)
#     for num in nums:
#         countArr[num - minElem] += 1
#     starting_index = 0
#     for i, cnt in enumerate(countArr):
#         countArr[i] = starting_index
#         starting_index += cnt
#     for i in range(len(nums) - 1, -1, -1):
#         outputArr[countArr[nums[i] - minElem]] = nums[i]
#         countArr[nums[i] - minElem] += 1
#     for i in range(len(nums)):
#         nums[i] = outputArr[i]
    
# def threeSum(nums):
#     res = []
#     for i in range(len(nums)):
#         if nums[i] > 0:
#             break
#         if i == 0 or nums[i - 1] != nums[i]:
#             twoSumII(nums, i, res)
#     return res

# def twoSumII(nums, i, res):
#     j, k = i + 1, len(nums) - 1
#     while j < k:
#         tripletSum = nums[i] + nums[j] + nums[k]
#         if tripletSum > 0:
#             k -= 1
#         elif tripletSum < 0:
#             j += 1
#         else:
#             res.append([nums[i], nums[j], nums[k]])
#             j += 1
#             k -= 1
#             while j < k and nums[j] == nums[j - 1]:
#                 j += 1

# nums = [-2,0,1,1,2]
# countSort(nums)
# print(threeSum(nums))




# 4Sum
# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.

# def countSort(nums, placeVal):
#     countArr = [0] * 10
#     outputArr = [0] * len(nums)
#     for num in nums:
#         digit = (num // placeVal) % 10
#         countArr[digit] += 1
#     startingIndex = 0
#     for i, cnt in enumerate(countArr):
#         countArr[i] = startingIndex
#         startingIndex += cnt
#     for num in nums:
#         digit = (num // placeVal) % 10
#         outputArr[countArr[digit]] = num
#         countArr[digit] += 1
#     for i in range(len(nums)):
#         nums[i] = outputArr[i]

# def radixSort(nums):
#     minElem = min(nums)
#     nums[:] = [num - minElem for num in nums]
#     maxElem = max(nums)
#     placeVal = 1
#     while placeVal <= maxElem:
#         countSort(nums, placeVal)
#         placeVal *= 10
#     nums[:] = [num + minElem for num in nums]

# def kSum(nums, target, k):
#     res = []
#     if not nums:
#         return res
#     radixSort(nums)
#     averageVal = target // k
#     if averageVal < nums[0] or nums[-1] < averageVal:
#         return res
#     if k == 2:
#         return twoSum(nums, target)
#     for i in range(len(nums)):
#         if i == 0 or nums[i] != nums[i - 1]:
#             for subset in kSum(nums[i + 1:], target - nums[i], k - 1):
#                 res.append([nums[i]] + subset)
#     return res

# def twoSum(nums, target):
#     left, right = 0, len(nums) - 1
#     res = []
#     while left < right:
#         cur_sum = nums[left] + nums[right]
#         if cur_sum < target or (left > 0 and nums[left] == nums[left - 1]):
#             left += 1
#         elif cur_sum > target or (right < len(nums) - 1 and nums[right] == nums[right + 1]):
#             right -= 1
#         else:
#             res.append([nums[left], nums[right]])
#             right -= 1
#             left += 1
#     return res

# nums = [1,0,-1,0,-2,2]
# target = 8

# print(nums)
# print(kSum(nums, target, 4))




# Top K Frequent Elements
# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# from collections import Counter

# def partition(left, right):
#     pivotFrequency = count[unique[right]]
#     j = left
#     for i in range(left, right):
#         if count[unique[i]] <= pivotFrequency:
#             unique[j], unique[i] = unique[i], unique[j]
#             j += 1
#     unique[right], unique[j] = unique[j], unique[right]
#     return j

# def kFrequent(left, right, k):
#     if left == right:
#         return
#     pi = partition(left, right)
#     if k == pi:
#         return
#     elif k < pi:
#         kFrequent(left, pi - 1, k)
#     else:
#         kFrequent(pi + 1, right, k)

# nums = [1,1,1,2,2,3]
# k = 2
# count = Counter(nums)
# unique = list(count.keys())
# n = len(unique)
# kFrequent(0, n - 1, n - k)
# print(unique[n - k:])




# tasks.py # 4
# milestones = [5,2,1]
# _sum, _max = sum(milestones), max(milestones)
# if _sum - _max >= _max:
#     print(_sum)
# else:
#     print(2 * (_sum - _max) + 1)




# Subarray Sums Divisible by K
# Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.

# nums = [4,5,0,-2,-3,1]
# k = 5
# d = {0: 1}
# prefSum, res = 0, 0
# for num in nums:
#     prefSum += num
#     rem = prefSum % k
#     if rem in d:
#         res += d[rem]
#         d[rem] += 1
#     else:
#         d[rem] = 1
# print(res)        


# prefMod = [0] * k
# prefMod[0] = 1
# prefSum = 0
# for num in nums:
#     prefSum += num
#     prefMod[prefSum % k] += 1
# res = 0
# for mod in prefMod:
#     res += mod * (mod - 1) // 2
# print(res)




# d = {1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC", 50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"}
# num = 478
# res = []
# for value, symbol in d.items():
#     if num == 0:
#         break
#     count, num = divmod(num, value)
#     res.append(symbol * count)
# print("".join(res))




# Longest Substring with At Most Two Distinct Characters
# Given a string s, return the length of the longest substring that contains at most two distinct characters.

# from collections import defaultdict
# s = "ccaabbb"
# seen = defaultdict()
# maxLen = 0
# left, right = 0, 0
# while right < len(s):
#     seen[s[right]] = right
#     right += 1
#     if len(seen) == 3:
#         idx = min(seen.values())
#         del seen[s[idx]]
#         left = idx + 1
#     maxLen = max(maxLen, right - left)
# print(maxLen)




# Max Consecutive Ones III
# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

# nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
# k = 3
# numOfZeroes = 0
# maxSoFar = 0
# left, right = 0, 0
# while right < len(nums):
#     if nums[right] == 0:
#         numOfZeroes += 1
#     while numOfZeroes == k + 1:
#         if nums[left] == 0:
#             numOfZeroes -= 1
#         left += 1
#     maxSoFar = max(maxSoFar, right - left + 1)
#     right += 1
# print(maxSoFar)




# Subarray Sum Equals K
# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

# d = {0:1}
# nums = [1,-1,0]
# k = 0
# prefSum = 0
# cnt = 0
# for num in nums:
#     prefSum += num
#     if prefSum - k in d:
#         cnt += d[prefSum - k]
#     if prefSum not in d:
#         d[prefSum] = 1
#     else:
#         d[prefSum] += 1
# print(cnt)




# Longest Repeating Character Replacement
# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. 
# You can perform this operation at most k times.
# Return the length of the longest substring containing the same letter you can get after performing the above operations.

# from collections import defaultdict
# s = "ABAB"
# k = 2
# d = defaultdict(int)
# i = 0
# maxFreq = 0
# maxLen = 0
# for j in range(len(s)):
#     d[s[j]] += 1
#     maxFreq = max(maxFreq, d[s[j]])
#     valid = (j + 1 - i - maxFreq <= k)
#     if not valid:
#         d[s[i]] -= 1
#         i += 1
#     maxLen = j + 1 - i
# print(maxLen)




# Minimum Number of Days to Make m Bouquets
# You are given an integer array bloomDay, an integer m and an integer k.
# You want to make m bouquets. To make a bouquet, you need to use k adjacent flowers from the garden.
# The garden consists of n flowers, the ith flower will bloom in the bloomDay[i] and then can be used in exactly one bouquet.

# bloomDay = [1,10,3,10,2]
# m = 3
# k = 2
# left, right = 0, max(bloomDay)
# while left < right:
#     mid = (left + right) // 2
#     flowers, bouquets = 0, 0
#     for bloom in bloomDay:
#         flowers = 0 if bloom > mid else flowers + 1
#         if flowers >= k:
#             flowers = 0
#             bouquets += 1
#             if bouquets == m:
#                 break
#     if bouquets == m:
#         right = mid
#     else:
#         left = mid + 1
# print(left)




# from collections import defaultdict
# time = [60,60,60]
# d = defaultdict(int)
# for t in time:
#     d[t % 60] = d[t % 60] + 1

# res = d[0] * (d[0] - 1) // 2 + d[30] * (d[30] - 1) // 2 

# for t in range(1, 29):
#     res += d[t] * d[60 - t]
# print(res)


# time = [30,20,150,100,40]
# d = {}
# cnt = 0
# for min in time:
#     rem = min % 60
#     if rem not in d:
#         d[rem] = 1
#     else:
#         d[rem] += 1
# print(d)
# for rem in d.keys():
#     if (60 - rem) % 60 == rem:
#         cnt += (d[rem] * (d[rem] - 1))
#     elif (60 - rem) in d:
#         cnt += d[rem] * d[60 - rem]
# print(cnt // 2)




# Open the Lock
# You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. 
# The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. Each move consists of turning one wheel 
# one slot.
# The lock initially starts at '0000', a string representing the state of the 4 wheels.
# You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you 
# will be unable to open it.
# Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the 
# lock, or -1 if it is impossible.

# from collections import deque
# deadends = ["0201","0101","0102","1212","2002"]
# target = "0202"
# def combinations(lock):
#     for i in range(4):
#         wheel  = int(lock[i])
#         for move in (-1, 1):
#             newWheel = (wheel + move) % 10
#             yield lock[:i] + str(newWheel) + lock[i+1:]
# queue = deque([("0000", 0)])
# deadends = set(deadends)
# seen = {"0000"}
# while queue:
#     curr, lvl = queue.popleft()
#     if curr == target:
#         print(lvl)
#         break
#     if curr in deadends:
#         continue
#     for combination in combinations(curr):
#         if combination not in seen:
#             queue.append((combination, lvl + 1))
#             seen.add(combination)
# print(-1)




# Find the Winner of the Circular Game
# The rules of the game are as follows:
# Start at the 1st friend.
# Count the next k friends in the clockwise direction including the friend you started at. The counting wraps around the circle and may count some 
# friends more than once.
# The last friend you counted leaves the circle and loses the game.
# If there is still more than one friend in the circle, go back to step 2 starting from the friend immediately clockwise of the friend who just 
# lost and repeat.
# Else, the last friend in the circle wins the game.
# Given the number of friends, n, and an integer k, return the winner of the game.

# n = 5
# k = 2
# def winner(n, k):
#     if n == 1:
#         return 0
#     return (winner(n - 1, k) + k) % n
# print(winner(n, k) + 1)




# Maximum Sum Circular Subarray
# Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.

# nums = [5,-3,5]
# maxSoFar = float("-inf")
# currMax = 0
# minSoFar = float("inf")
# currMin = float("inf")
# for i in range(len(nums)):
#     if currMin > 0:
#         currMin = nums[i]
#     else:
#         currMin += nums[i]
#     minSoFar = min(minSoFar, currMin)

#     currMax += nums[i]
#     maxSoFar = max(currMax, maxSoFar)
#     if currMax < 0:
#         currMax = 0
# total_sum = sum(nums)
# if total_sum == minSoFar:
#     print(maxSoFar)
# else:
#     print(max(maxSoFar, total_sum - minSoFar))




# Sliding Window Maximum
# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. 
# You can only see the k numbers in the window. Each time the sliding window moves right by one position.
# Return the max sliding window.

# from collections import deque
# queue = deque()
# res = []
# nums = [1,3,-1,-3,-2,-4,5,3,6,7]
# k = 3
# def clean(i):
#     if queue and queue[0] == i - k:
#         queue.popleft()
#     while queue and nums[i] > nums[queue[-1]]:
#         queue.pop()
# max_elem = 0
# for i in range(k):
#     clean(i)
#     queue.append(i)
#     if nums[i] > max_elem:
#         max_elem = nums[i]
# res.append(max_elem)
# for i in range(k, len(nums)):
#     clean(i)
#     queue.append(i)
#     res.append(nums[queue[0]])
# print(res)


# nums = [1,3,-1,-3,5,3,6,7]
# k = 3
# n = len(nums)
# res = []
# left = [0] * n
# left[0] = nums[0]
# right = [0] * n
# right[n - 1] = nums[n - 1]

# for i in range(1, n):
#     if i % k == 0:
#         left[i] = nums[i]
#     else:
#         left[i] = max(left[i - 1], nums[i])
    
#     j = n - i - 1
#     if (j + 1) % k == 0:
#         right[j] = nums[j]
#     else:
#         right[j] = max(right[j + 1], nums[j])
# for i in range(n - k + 1):
#     res.append(max(left[i + k - 1], right[i]))
# print(res)




# Minimum Window Substring
# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t 
# (including duplicates) is included in the window. If there is no such substring, return the empty string "".
 
# from collections import Counter, defaultdict
# s = "ADOBECODEBANC"
# t = "ABC"
# # res = [float("inf"), None, None]
# # subs = Counter(t)
# # d = defaultdict(int)
# # left, right = 0, 0
# # cnt = 0
# # while right < len(s):
# #     d[s[right]] += 1
# #     if s[right] in subs and d[s[right]] == subs[s[right]]:
# #         cnt += 1
# #     while left <= right and cnt == len(subs):
# #         if right - left + 1 < res[0]:
# #             res = [right - left + 1, left, right]
# #         d[s[left]] -= 1
# #         if s[left] in subs and d[s[left]] < subs[s[left]]:
# #             cnt -= 1
# #         left += 1
# #     right += 1
# # print(res)


# res = [float("inf"), None, None]
# subs = Counter(t)
# d = defaultdict(int)
# left, right = 0, 0
# cnt = 0
# s_with_no_dupl = []
# for i in range(len(s)):
#     if s[i] in subs:
#         s_with_no_dupl.append((i, s[i]))

# while right < len(s_with_no_dupl):
#     char = s_with_no_dupl[right][1]
#     d[char] += 1
#     if d[char] == subs[char]:
#         cnt += 1
#     while left <= right and cnt == len(subs):
#         char = s_with_no_dupl[left][1]
#         start = s_with_no_dupl[left][0]
#         end = s_with_no_dupl[right][0]
#         if end - start + 1 < res[0]:
#             res = [end - start + 1, start, end]
#         d[char] -= 1
#         if d[char] < subs[char]:
#             cnt -= 1
#         left += 1
#     right += 1
# print(res)




# Palindrome Linked List
# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
        
# class Solution:
#     def isPalindrome(self, head: Optional[ListNode]) -> bool:
#         if not head:
#             return True
        
#         firstHalfEnd = self.endOfTheFirstHalf(head)
#         secondHalfStart = self.reverseLinkedList(firstHalfEnd.next)

#         res = True
#         first = head
#         second = secondHalfStart
#         while res and second:
#             if first.val != second.val:
#                 res = False
#             first = first.next
#             second = second.next

#         firstHalfEnd.next = self.reverseLinkedList(secondHalfStart)
#         return res

#     def endOfTheFirstHalf(self, head):
#         hare = head 
#         tortoise = head
#         while hare.next and hare.next.next:
#             hare = hare.next.next
#             tortoise = tortoise.next
#         return tortoise

#     def reverseLinkedList(self, head):
#         prev = None
#         curr = head
#         while curr:
#             next_node = curr.next
#             curr.next = prev
#             prev = curr
#             curr = next_node
#         return prev




# Decode String
# "abcabccdcdcdef"

# s = "2[abc]3[cd]ef"
# stack = []
# def ss(stack) -> str:
#     return stack[-1]
# for i in range(len(s)):
#     if s[i] == "]":
#         stringBuilder = []
#         while stack[-1] != "[":
#             stringBuilder.append(stack.pop())
#         stack.pop()
#         base = 1
#         k = 0
#         while stack and ss(stack).isdigit():
#             k += int(stack.pop()) * base
#             base *= 10
#         while k != 0:
#             for j in range(len(stringBuilder) - 1, -1, -1):
#                 stack.append(stringBuilder[j])
#             k -= 1
#     else:
#         stack.append(s[i])
# print("".join(stack))




# Remove All Adjacent Duplicates in String II
# "aa"
# s = "deeedbbcccbdaa"
# k = 3
# cnt = []
# stack = []
# for i in range(len(s)):
#     if not stack or s[i] != stack[-1]:
#         cnt.append(1)
#     else:
#         cnt[-1] += 1
#     stack.append(s[i])
#     if cnt[-1] == k:
#         for j in range(k):
#             stack.pop()
#         cnt.pop()
# print("".join(stack))




# Largest Rectangle in Histogram
# Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest 
# rectangle in the histogram.
# heights = [2,1,5,6,2,3]

# def area(heights, start, end):
#     if start > end:
#         return 0
#     min_index = start
#     for i in range(start, end + 1):
#         if heights[min_index] > heights[i]:
#             min_index = i
#     return max(
#         heights[min_index] * (end - start + 1),
#         area(heights, start, min_index - 1),
#         area(heights, min_index + 1, end)
#     )
# print(area(heights, 0, len(heights) - 1))


# stack = [-1]
# max_area = 0
# for i in range(len(heights)):
#     while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
#         curr_height = heights[stack.pop()]
#         curr_width = i - stack[-1] - 1
#         max_area = max(max_area, curr_height * curr_width)
#     stack.append(i)
# while stack[-1] != -1:
#     curr_height = heights[stack.pop()]
#     curr_width = len(heights) - stack[-1] - 1
#     max_area = max(max_area, curr_height * curr_width)
# print(max_area)




# Asteroid Collision
# We are given an array asteroids of integers representing asteroids in a row.
# For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). 
# Each asteroid moves at the same speed.
# Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, 
# both will explode. Two asteroids moving in the same direction will never meet.

# asteroids = [5,2,-5]
# stack = []
# for new in asteroids:
#     while stack and new < 0 < stack[-1]:
#         if stack[-1] < -new:
#             stack.pop()
#             continue
#         elif stack[-1] == -new:
#             stack.pop()
#         break
#     else:
#         stack.append(new)
# print(stack)




# Next Greater Element II
# Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every 
# element in nums. The next greater number of a number x is the first greater number to its traversing-order next in the array, which means you 
# could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.

# nums = [1,2,1]
# # nums = [1,2,3,4,3]
# stack = []
# n = len(nums)
# res = [0] * n
# for i in range(n * 2 - 1, -1, -1):
#     while stack and nums[stack[-1]] <= nums[i % n]:
#         stack.pop()
#     if not stack:
#         res[i % n] = -1
#     else:
#         res[i % n] = nums[stack[-1]]
#     stack.append(i % n)
# return res




# num1 = "0"
# num2 = "0"
# carry = 0
# res = []
# n1 = len(num1) - 1
# n2 = len(num2) - 1
# while n1 >= 0 or n2 >= 0:
#     digit1 = ord(num1[n1]) - ord('0') if n1 >= 0 else 0
#     digit2 = ord(num2[n2]) - ord('0') if n2 >= 0 else 0
#     sum_ = (digit1 + digit2 + carry) % 10
#     carry = (digit1 + digit2 + carry) // 10
#     res.append(str(sum_))
#     n1 -= 1
#     n2 -= 1
# if carry:
#     res.append(str(carry))
# print("".join(res[::-1]))



# Kth Smallest Element in a Sorted Matrix
# Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix.

# def binarySearch(matrix, mid, smaller, larger):
#     count, n = 0, len(matrix)
#     row, col = n - 1, 0
#     while row >= 0 and col < n:
#         if matrix[row][col] > mid:
#             larger = min(larger, matrix[row][col])
#             row -= 1
#         else:
#             smaller = max(smaller, matrix[row][col])
#             count += row + 1
#             col += 1
#     return count, smaller, larger

# def kthSmallest(matrix, k) -> int:
#     n = len(matrix)
#     start, end = matrix[0][0], matrix[n-1][n-1]
#     while start < end:
#         smaller, larger = matrix[0][0], matrix[n-1][n-1]
#         mid = start + (end - start) / 2
#         count, smaller, larger = binarySearch(matrix, mid, smaller, larger)
#         if count == k:
#             return smaller
#         elif count < k:
#             start = larger
#         else:
#             end = smaller
#     return start

# matrix = [[1,5,9],[10,11,13],[12,13,15]]
# k = 8
# print(kthSmallest(matrix, k))




# Search for a Range
# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
# If target is not found in the array, return [-1, -1].

# nums = [5,6,7,8,9,10]
# target = 4

# def binaryLeft(left, right):
#     found = False
#     while left < right:
#         mid = (left + right) // 2
#         if nums[mid] == target:
#             found = True
#         if nums[mid] < target:
#             left = mid + 1
#         else:
#             right = mid
#     return left, found

# def binaryRight(left, right):
#     while left < right:
#         mid = (left + right) // 2
#         if target < nums[mid]:
#             right = mid
#         else:
#             left = mid + 1
#     return left

# found = binaryLeft(0, len(nums))
# if found[1]:
#     print([found[0], binaryRight(0, len(nums)) - 1])
# else:
#     print([-1, -1])



# Minimum Genetic Mutation
# A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.
# Suppose we need to investigate a mutation from a gene string startGene to a gene string endGene where one mutation is defined as one single 
# character changed in the gene string.
# For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
# There is also a gene bank bank that records all the valid gene mutations. A gene must be in bank to make it a valid gene string.
# Given the two gene strings startGene and endGene and the gene bank bank, return the minimum number of mutations needed to mutate from startGene 
# to endGene. If there is no such a mutation, return -1.
# Note that the starting point is assumed to be valid, so it might not be included in the bank.

# from collections import deque
# startGene = "AACCGGTT"
# endGene = "AAACGGTA"
# bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
# queue = deque([(startGene, 0)])
# seen = {startGene}
# while queue:
#     interimGene, step = queue.popleft()
#     if interimGene == endGene:
#         print(step)
#         break
#     for char in "ACGT":
#         for i in range(len(interimGene)):
#             nei = interimGene[:i] + char + interimGene[i+1:]
#             if nei not in seen and nei in bank:
#                 queue.append((nei, step + 1))
#                 seen.add(nei)
# print(-1)




# Find Minimum in Rotated Sorted Array
# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] 
# might become:
# [4,5,6,7,0,1,2] if it was rotated 4 times.
# [0,1,2,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
# Given the sorted rotated array nums of unique elements, return the minimum element of this array.

# def binarySearch(left, right):
#     while left < right:
#         mid = left + (right - left) // 2
#         if nums[mid] < nums[right]:
#             right = mid
#         else:
#             left = mid + 1
#     return left

# nums = [11,13,15,17]
# print(nums[binarySearch(0, len(nums) - 1)])




# Find the Duplicate Number
# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
# There is only one repeated number in nums, return this repeated number.
# You must solve the problem without modifying the array nums and uses only constant extra space.

# nums = [1,3,4,2,2]
# hare = tortoise = nums[0]
# while True:
#     tortoise = nums[tortoise]
#     hare = nums[nums[hare]]
#     if tortoise == hare:
#         break
# tortoise = nums[0]
# while tortoise != hare:
#     tortoise = nums[tortoise]
#     hare = nums[hare]
# print(hare)





# lst = input().split()
# for i in range(len(lst)):
    # if lst[i:] == lst[i:][::-1]:
        # print(i)
        # print(*lst[:i][::-1])
        # break




# n = 2
# k = 1
# def kthElement(n , k):
#     if n == 1:
#         return 0
#     res = kthElement(n - 1, (k + 1) // 2)
#     if not res:
#         return abs((k % 2) - 1)
#     else:
#         return (k % 2)
    
# print(kthElement(n, k))
