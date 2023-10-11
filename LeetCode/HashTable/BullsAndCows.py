# You are playing the Bulls and Cows game with your friend.

# You write down a secret number and ask your friend to guess what the number is. When your friend makes a guess, you provide a 
# hint with the following info:

    # The number of "bulls", which are digits in the guess that are in the correct position.
    # The number of "cows", which are digits in the guess that are in your secret number but are located in the wrong position. 
    # Specifically, the non-bull digits in the guess that could be rearranged such that they become bulls.

# Given the secret number secret and your friend's guess guess, return the hint for your friend's guess.

# The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows. Note that both secret and
# guess may contain duplicate digits.

def getHint(secret, guess):
    possible_cows = {}
    cnt_bulls = 0
    cnt_cows = 0

    for i in range(len(secret)):
        if secret[i] == guess[i]:
            cnt_bulls += 1
        else:
            possible_cows[secret[i]] = possible_cows.get(secret[i], 0) + 1
        
    for j in range(len(guess)):
        if guess[j] in possible_cows and guess[j] != secret[j] and possible_cows[guess[j]] != 0:
            cnt_cows += 1
            possible_cows[guess[j]] -= 1

    return str(cnt_bulls) + 'A' + str(cnt_cows) + 'B'


secret = "1807"
guess = "7810"
# Output: "1A3B"
# Explanation: Bulls are connected with a '|' and cows are underlined:
# "1807"
#   |
# "7810"
#  _ __

print(getHint(secret, guess))


secret = "1123"
guess = "0111"
# Output: "1A1B"
# Explanation: Bulls are connected with a '|' and cows are underlined:
# "1123"        "1123"
#   |      or     |
# "0111"        "0111"
#    _              _
# Note that only one of the two unmatched 1s is counted as a cow since the non-bull digits can only be rearranged to allow
#  one 1 to be a bull.

print(getHint(secret, guess))