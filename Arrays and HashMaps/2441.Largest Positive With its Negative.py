class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        res = -1
        visited = set()
        for n in nums:
            if -n in visited:
                res = max(res, abs(n))
            else:
                visited.add(n)
        return res
                    
