class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res = [0,0]   #[duplicate,missing]
        from collections import Counter
        hashMap = Counter(nums)
        for n in range(1,len(nums)+1):
            if hashMap[n] == 2:
                res[0] = n
            if hashMap[n] == 0:
                res[1] = n
        return res         
