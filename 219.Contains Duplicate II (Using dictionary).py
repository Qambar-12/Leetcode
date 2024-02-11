def containsNearbyDuplicate(nums, k):
    dic = {}
    for index, element in enumerate(nums):
        if (element in dic) and index - dic[element] <= k:
            return True
        dic[element] = index
    return False
