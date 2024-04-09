class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = []
        runningTotal = 0
        for n in nums:
            runningTotal += n
            self.prefix.append(runningTotal)

    def sumRange(self, left: int, right: int) -> int:  
        r = self.prefix[right] 
        #because the total is inclusive indices
        l = self.prefix[left - 1] if left > 0 else 0
        return r - l

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)