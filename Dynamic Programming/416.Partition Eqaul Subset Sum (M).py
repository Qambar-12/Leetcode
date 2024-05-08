class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #we can solve this question using DYNAMIC PROGRAMMING (sort of backtracking technique)
        #Obs 1 : if we break into equal sums each subset sum must be equal to sum(nums)/2
        #so if we have we have any resulting odd number sum of nums so its division would be fractional
        #and thus since it cannot positive integers cannot sum up to decimals we can simply return false

        #Observation 2 : we now make a sort decision tree where at every point we could include it in our sum or not
        #if ever the sum in hashset becomes equal to our target = (sum(nums)/2) then we can return True
        dp_set = set()
        dp_set.add(0)       #the default value of sum is zero to get things started
        if sum(nums) % 2:
            return False
        target = (sum(nums))//2    
        #we can also run the loop in reverse order
        for i in range(len(nums)):
            nextDP = set()
            for t in dp_set:
                #if we find the target we can immediately return True
                if t + nums[i] == target:
                    return True
                #we then add both possibilites to the set if we include or skip the number
                nextDP.add(t+nums[i])
                nextDP.add(t)
            dp_set = nextDP            
        return False             

