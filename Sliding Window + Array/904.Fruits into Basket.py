import collections
def totalFruit(fruits):
    #Sliding window technique
    """creates a defaultdict where the default value for new entries is 0. This is commonly used when you want to count occurrences of items, as it allows you to simply increment the count for each item without needing to check if the item is already in the dictionary."""
    count = collections.defaultdict(int)
    i ,total, res = 0,0,0
    for j in range(len(fruits)):
        count[fruits[j]] += 1
        total += 1
        #There are more than 2 fruits in basket i.e size of window exceeds
        while len(count) > 2:
            f = fruits[i]
            count[f] -= 1
            total -= 1
            i += 1
            if not count[f]:
                del count[f]
        res = max(res,total)    
    return res    