class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # l , r = 0 , len(nums)-1
        # while l <= r:
        #     m = (l+r)//2
        #     if nums[m] < target:
        #         l = m+1
        #     elif nums[m] > target:
        #         r = m-1
        #     else:
        #         i , j = m , m
        #         res1,res2 = m , m
        #         while i >= 0 or j < len(nums):
        #             if i >=0 and  nums[i] == target:
        #                 res1 = i
        #             if j < len(nums) and  nums[j] == target:
        #                 res2 = j
        #             i-=1
        #             j+=1    
        #         return [res1,res2]  
        # return [-1,-1]                

        #BINARY SEARCH : calling function twice once searching for leftmost occurecnce and the other time for right most occurence of target value
        left = self.binSearch(nums,target,True)
        right = self.binSearch(nums,target,False)
        return [left,right]

    def binSearch(self,nums,target,searchLeftMostOccurence):
        l , r = 0 , len(nums)-1
        i = -1
        while l <= r:
            m = (l+r)//2
            if nums[m] < target:
                l = m+1
            elif nums[m] > target:
                r = m-1
            else:
                i = m
                if searchLeftMostOccurence:
                    r = m-1
                else:
                    l = m+1
        return i                
    
