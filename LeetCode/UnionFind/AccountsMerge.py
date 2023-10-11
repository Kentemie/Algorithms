# Given a list of accounts where each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and
# the rest of the elements are emails representing emails of the account.

# Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some common email to both
# accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name.
# A person can have any number of accounts initially, but all of their accounts definitely have the same name.

# After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest
# of the elements are emails in sorted order. The accounts themselves can be returned in any order.


class UnionFind:

    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX == rootY:
            return False

        if self.rank[rootX] > self.rank[rootY]:
            self.root[rootY] = rootX
        elif self.rank[rootX] < self.rank[rootY]:
            self.root[rootX] = rootY
        else:
            self.root[rootY] = rootX
            self.rank[rootX] += 1
        
        return True 


def accountsMerge(accounts):
    uf = UnionFind(len(accounts))
    email_to_account = {}

    for i in range(len(accounts)):
        for email in accounts[i][1:]:
            if email in email_to_account:
                uf.union(i, email_to_account[email])
            else:
                email_to_account[email] = i
    
    email_group = {}

    for email, idx in email_to_account.items():
        root = uf.find(idx)
        email_group.setdefault(root, []).append(email)

    res = []
    
    for idx, emails in email_group.items():
        name = accounts[idx][0]
        res.append([name] + sorted(emails))

    return res



accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],
            ["John","johnsmith@mail.com","john00@mail.com"],
            ["Mary","mary@mail.com"],
            ["John","johnnybravo@mail.com"]]

print(accountsMerge(accounts))