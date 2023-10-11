# The set [1, 2, 3, ..., n] contains a total of n! unique permutations.

# By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

    # "123"
    # "132"
    # "213"
    # "231"
    # "312"
    # "321"

# Given n and k, return the kth permutation sequence.



# Algorithm:

# The factorial number system is a mixed radix numeral system: the i-th digit from the right has base i, which means
# that the digit must be strictly less than i, and that (taking into account the bases of the less significant digits) 
# its value is to be multiplied by (i − 1)! (its place value).

# For example, 46310 can be transformed into a factorial representation by these successive divisions:

    # 463 ÷ 1 = 463, remainder 0
    # 463 ÷ 2 = 231, remainder 1
    # 231 ÷ 3 = 77, remainder 0
    # 77 ÷ 4 = 19, remainder 1
    # 19 ÷ 5 = 3, remainder 4
    # 3 ÷ 6 = 0, remainder 3

# The process terminates when the quotient reaches zero. Reading the remainders backward gives 3:4:1:0:1:0!.

# The process may become clearer with a longer example. Let's say we want the 2982nd permutation of the numbers 0 through 6. 
# The number 2982 is 4:0:4:1:0:0:0! in factoradic, and that number picks out digits (4,0,6,2,1,3,5) in turn, via indexing a 
# dwindling ordered set of digits and picking out each digit from the set at each turn:

                            # 4:0:4:1:0:0:0!  ─►  (4,0,6,2,1,3,5)
# factoradic: 4              :   0            :   4          :   1        :   0      :   0    :   0!
            # ├─┬─┬─┬─┐          │                ├─┬─┬─┬─┐      ├─┐          │          │        │
# sets:      (0,1,2,3,4,5,6) ─► (0,1,2,3,5,6) ─► (1,2,3,5,6) ─► (1,2,3,5) ─► (1,3,5) ─► (3,5) ─► (5)
                    # │          │                        │        │          │          │        │
# permutation:       (4,         0,                       6,       2,         1,         3,       5)


def getPermutation(n, k):
    k -= 1
    radix = 1 
    factoradics = [0] * (n + 1)

    while k > 0:
        factoradics[radix] = (k % radix)
        k //= radix
        radix += 1

    indices = [False] * (n + 1)

    print(factoradics)

    def f(i):
        j = 1
        while j <= n:
            if indices[j]:
                j += 1
                continue
            if i == 0:
                indices[j] = True
                return str(j)
            i -= 1
            j += 1
    
    res = []

    for factoradic in factoradics[:0:-1]:
        res.append(f(factoradic))

    return "".join(res)

n = 3
k = 3

n = 4
k = 9 

n = 3
k = 1 

n = 3
k = 2

print(getPermutation(n, k))