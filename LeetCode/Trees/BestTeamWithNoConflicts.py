def bestTeamScore(scores, ages):

    # Query tree to get the maximum score up to this age.
    def queryBIT(age):
        maxScore = 0
        i = age
        while i > 0:
            maxScore = max(maxScore, BIT[i])
            i -= i & (-i)
        return maxScore
    
    # Update the maximum score for all the nodes with an age greater than the given age.
    def updateBIT(age, currentBestScore):
        i = age
        while i < len(BIT):
            BIT[i] = max(BIT[i], currentBestScore)
            i += i & (-i)


    score_age_pair = sorted(zip(scores, ages))

    highest_age = 0

    for age in ages:
        highest_age = max(highest_age, age)

    BIT = [0] * (highest_age + 1)
    res = 0

    for score, age in score_age_pair:
        currentBestScore = score + queryBIT(age)
        updateBIT(age, currentBestScore)
        res = max(res, currentBestScore)

    return res

scores = [4,5,6,5]
ages = [2,1,2,1]

# scores = [1,2,3,5]
# ages = [8,9,10,1]

# scores = [1,3,5,10,15]
# ages = [1,2,3,4,5]

print(bestTeamScore(scores, ages))