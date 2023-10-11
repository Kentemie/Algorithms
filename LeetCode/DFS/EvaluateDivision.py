# You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] 
# and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

# You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer 
# for Cj / Dj = ?.

# Return the answers to all queries. If a single answer cannot be determined, return -1.0.

# Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that
# there is no contradiction.


def calcEquation(equations, values, queries):

    def DFS(dividend, divisor, product, seen):
        quotient = -1
        seen.add(dividend)
        divisors = graph[dividend]

        if divisor in divisors:
            quotient = product * divisors[divisor]
        else:
            for div, value in divisors.items():
                if div in seen:
                    continue
                
                quotient = DFS(div, divisor, product * value, seen)
                
                if quotient != -1:
                    break
        
        seen.remove(dividend)

        return quotient
    
    graph = {}

    for (dividend, divisor), value in zip(equations, values):
        divisors = graph.setdefault(dividend, {})
        divisors.setdefault(divisor, value)
        
        divisors = graph.setdefault(divisor, {})
        divisors.setdefault(dividend, 1 / value)

    results = []

    for dividend, divisor in queries:

        if dividend not in graph or divisor not in graph:
            quotient = -1.0
        elif dividend == divisor:
            quotient = 1.0
        else:
            quotient = DFS(dividend, divisor, 1, set())

        results.append(quotient)

    return results


equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
# [6.00000,0.50000,-1.00000,1.00000,-1.00000]

equations = [["a","b"],["b","c"],["bc","cd"]]
values = [1.5,2.5,5.0]
queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
# [3.75000,0.40000,5.00000,0.20000]

equations = [["a","b"]]
values = [0.5]
queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
# [0.50000,2.00000,-1.00000,-1.00000]

print(calcEquation(equations, values, queries))