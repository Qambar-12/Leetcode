def topKFrequent(nums,k):
    from collections import Counter
    arr = []
    res = []
    dic = Counter(nums)
    for key , value in dic.items():
        arr.append([value,key])
    arr.sort(reverse=True)
    for pair in range(k):
        res.append(arr[pair][1])
    return res