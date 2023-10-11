# You want to schedule a list of jobs in d days. Jobs are dependent (i.e To work on the ith job, you have to finish all the jobs j 
# where 0 <= j < i).
# You have to finish at least one task every day. The difficulty of a job schedule is the sum of difficulties of each day of the d days. The 
# difficulty of a day is the maximum difficulty of a job done on that day.
# You are given an integer array jobDifficulty and an integer d. The difficulty of the ith job is jobDifficulty[i].
# Return the minimum difficulty of a job schedule. If you cannot find a schedule for the jobs return -1.

from functools import lru_cache

@lru_cache(None)
def findMinSchedule(i, day):
    if day == d:
        return hardest_job_remaining[i]
    hardest = 0
    best = float('inf')

    for j in range(i, n - (d - day)):
        hardest = max(hardest, jobDifficulty[j])
        best = min(best, hardest + findMinSchedule(j + 1, day + 1))

    return best

jobDifficulty = [6,5,4,3,2,1]
d = 2
n = len(jobDifficulty)

hardest_job = 0
hardest_job_remaining = [0] * n

for i in range(n - 1, -1, -1):
    hardest_job = max(hardest_job, jobDifficulty[i])
    hardest_job_remaining[i] = hardest_job

print(findMinSchedule(0, 1))