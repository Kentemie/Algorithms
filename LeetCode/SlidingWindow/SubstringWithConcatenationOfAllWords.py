# You are given a string s and an array of strings words. All the strings of words are of the same length.

# A concatenated substring in s is a substring that contains all the strings of any permutation of words concatenated.

    # For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are
    #  all concatenated strings. "acdbef" is not a concatenated substring because it is not the concatenation of any 
    #  permutation of words.

# Return the starting indices of all the concatenated substrings in s. You can return the answer in any order.

from collections import Counter, defaultdict

def findSubstring(s, words):
    n = len(s)
    k = len(words)
    word_length = len(words[0])
    substring_length = k * word_length
    words_count = Counter(words)

    def sliding_window(left):
        words_found = defaultdict(int)
        words_used = 0
        excess_word = False

        # iterate word_length at a time, and at each iteration we focus on one word
        for right in range(left, n, word_length):
            if right + word_length > n:
                break

            subs = s[right : right + word_length]
            if subs not in words_count:
                # Mismatched word - reset the window
                words_found = defaultdict(int)
                words_used = 0
                excess_word = False 
                # Retry at the next index
                left = right + word_length 
            else:
                # If we reached max window size or have an excess word
                while right - left == substring_length or excess_word:
                    # Move the left bound over continously
                    leftmost_word = s[left : left + word_length]
                    left += word_length
                    words_found[leftmost_word] -= 1

                    if words_found[leftmost_word] == words_count[leftmost_word]:
                        # This word was the excess word
                        excess_word = False
                    else:
                        # Otherwise we actually needed it
                        words_used -= 1
                
                # Keep track of how many times this word occurs in the window
                words_found[subs] += 1
                if words_found[subs] <= words_count[subs]:
                    words_used += 1
                else:
                    # Found too many instances already
                    excess_word = True

                if words_used == k and not excess_word:
                    # Found a valid substring
                    result.append(left)

    result = []
    for i in range(word_length):
        sliding_window(i)

    return result

# s = "barfoothefoobarman"
# words = ["foo","bar"]

# s = "wordgoodgoodgoodbestword"
# words = ["word","good","best","word"]

# s = "barfoofoobarthefoobarman"
# words = ["bar","foo","the"]

s = "ababababab"
words = ["ababa","babab"]

print(findSubstring(s, words))