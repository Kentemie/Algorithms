# We are given n different types of stickers. Each sticker has a lowercase English word on it.

# You would like to spell out the given string target by cutting individual letters from your collection of stickers and
# rearranging them. You can use each sticker more than once if you want, and you have infinite quantities of each sticker.

# Return the minimum number of stickers that you need to spell out target. If the task is impossible, return -1.

# Note: In all test cases, all words were chosen randomly from the 1000 most common US English words, and target was chosen 
# as a concatenation of two random words.


def minStickers(stickers, target):
    n = len(target)
    maxMask = 1 << n

    # dp[i] := min number of stickers to spell out i, where i is the bit mask of target.
    dp = [float("inf")] * maxMask
    dp[0] = 0

    # Preprocess the stickers to create a mapping of character frequencies
    stickerCounts = []
    for sticker in stickers:
        counter = {}
        for char in sticker:
            counter[char] = counter.get(char, 0) + 1
        stickerCounts.append(counter)

    for mask in range(maxMask):
        if dp[mask] == float("inf"):
            continue

        for stickerCount in stickerCounts:
            if not any(char in stickerCount for char in target):
                continue
            superMask = mask

            for char_in_sticker, freq in stickerCount.items():

                for j, char_in_target in enumerate(target):
                    if char_in_sticker == char_in_target and not (superMask >> j & 1):
                        superMask |= 1 << j
                        freq -= 1
                        if freq == 0:
                            break

            dp[superMask] = min(dp[superMask], dp[mask] + 1)

    return dp[-1] if dp[-1] != float("inf") else -1

stickers = ["with","example","science"]
target = "thehat"

stickers = ["notice","possible"]
target = "basicbasic"

stickers = ["charge","mind","bottom"]
target = "centorder"

print(minStickers(stickers, target))