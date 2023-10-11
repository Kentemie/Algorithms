# You are the manager of a basketball team. For the upcoming tournament, you want to choose the team with the highest overall 
# score. The score of the team is the sum of scores of all the players in the team.

# However, the basketball team is not allowed to have conflicts. A conflict exists if a younger player has a strictly 
# higher score than an older player. A conflict does not occur between players of the same age.

# Given two lists, scores and ages, where each scores[i] and ages[i] represents the score and age of the ith player, 
# respectively, return the highest overall score of all possible basketball teams.

def bestTeamScore(scores, ages):
    people = sorted(zip(ages, scores))
    n = len(people)

    dp = [[-1] * n for _ in range(n)]
    
    def DFS(idx, prev):
        if idx == n:
            return 0
        if dp[idx][prev + 1] != -1:
            return dp[idx][prev + 1]
        
        if prev == -1 or people[idx][1] >= people[prev][1]:
            dp[idx][prev + 1] = max(DFS(idx + 1, prev), people[idx][1] + DFS(idx + 1, idx))
            return dp[idx][prev + 1]
        
        dp[idx][prev + 1] = DFS(idx + 1, prev)
        return dp[idx][prev + 1]
    
    return DFS(0, -1)
        

scores = [4,5,6,5]
ages = [2,1,2,1]

# scores = [1,2,3,5]
# ages = [8,9,10,1]

# scores = [1,3,5,10,15]
# ages = [1,2,3,4,5]

print(bestTeamScore(scores, ages))