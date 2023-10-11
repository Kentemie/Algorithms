# You are given a 0-indexed integer array tasks, where tasks[i] represents the difficulty level of a task. In each round, 
# you can complete either 2 or 3 tasks of the same difficulty level.

# Return the minimum rounds required to complete all the tasks, or -1 if it is not possible to complete all the tasks.

from collections import Counter

def minimumRounds(tasks):
    tasksFrequency = Counter(tasks)
    rounds = 0
    for _, freq in tasksFrequency.most_common():
        if freq < 2:
            return -1
        if freq % 3 == 0:
            rounds += freq // 3
        else:
            rounds += freq // 3 + 1
    return rounds

tasks = [2,2,3,3,2,4,4,4,4,4]
# 4
tasks = [2,3,3]
# -1
print(minimumRounds(tasks))