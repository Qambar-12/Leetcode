class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k == 0:
            return
        elif len(nums) > k:
            nums[:] = nums[-k:] + nums[:(len(nums) - k)]
        else:
            for i in range(k):
                nums.insert(0,nums[-1])
                nums.pop()


                
