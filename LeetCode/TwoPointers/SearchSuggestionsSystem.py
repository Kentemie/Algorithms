def suggestedProducts(products, searchWord):
    res = []
    l, r = 0, len(products) - 1
    products.sort()
    
    for i in range(len(searchWord)):
        char = searchWord[i]
        while l <= r and (len(products[l]) <= i or products[l][i] != char):
            l += 1
        while l <= r and (len(products[r]) <= i or products[r][i] != char):
            r -= 1
        res.append([])
        for j in range(min(3, r - l + 1)):
            res[-1].append(products[l + j])

    return res

products = ["mobile","mouse","moneypot","monitor","mousepad"]
searchWord = "mouse"

print(suggestedProducts(products, searchWord))