# You are given an integer array nums. Two players are playing a game with this array: player 1 and player 2.

# Player 1 and player 2 take turns, with player 1 starting first. Both players start the game with a score of 0. At each turn, 
# the player takes one of the numbers from either end of the array (i.e., nums[0] or nums[nums.length - 1]) which reduces the
# size of the array by 1. The player adds the chosen number to their score. The game ends when there are no more elements in the array.

# Return true if Player 1 can win the game. If the scores of both players are equal, then player 1 is still the winner, and you 
# should also return true. You may assume that both players are playing optimally.

def predictTheWinner(nums):
    memo = {}

    def DFS(left, right):
        if (left, right) in memo:
            return memo[(left, right)]
        if left == right:
            return nums[left]
        
        remove_first = nums[left] - DFS(left + 1, right)
        remove_last = nums[right] - DFS(left, right - 1)

        memo[(left, right)] = max(remove_first, remove_last)
        
        return memo[(left, right)]
    
    return DFS(0, len(nums) - 1) >= 0


nums = [1,5,233,7]
nums = [1,5,2]

print(predictTheWinner(nums))