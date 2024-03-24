class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index in range(len(nums)):
            Output = []
            for count in range(index+1,len(nums)):
                if (nums[index] + nums[count]) == target:
                    Output.append(index)
                    Output.append(count)
                    return Output








                
