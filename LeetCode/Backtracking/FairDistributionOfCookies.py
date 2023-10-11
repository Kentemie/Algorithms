# You are given an integer array cookies, where cookies[i] denotes the number of cookies in the ith bag. You are also given 
# an integer k that denotes the number of children to distribute all the bags of cookies to. All the cookies in the same bag
# must go to the same child and cannot be split up.

# The unfairness of a distribution is defined as the maximum total cookies obtained by a single child in the distribution.

# Return the minimum unfairness of all distributions.


def distributeCookies(cookies, k):
    distribution = [0] * k
    n = len(cookies)

    def DFS(i, remaining_children):
        if n - i < remaining_children:
            return float("inf")
        if i == n:
            return max(distribution)

        res = float("inf")

        for j in range(k):
            remaining_children -= int(distribution[j] == 0)
            distribution[j] += cookies[i]
            res = min(res, DFS(i + 1, remaining_children))
            distribution[j] -= cookies[i]
            remaining_children += int(distribution[j] == 0)

        return res

    return DFS(0, k)


cookies = [8,15,10,20,8]
k = 2

print(distributeCookies(cookies, k))