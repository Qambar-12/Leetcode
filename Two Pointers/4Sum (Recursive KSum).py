def fourSum(nums, target):
    #sorting so that all duplicates are adjacent to eachother
    nums.sort()
    #result holds all unique quadruplets and quad contains the current quadruplet
    res , quad = [] , []
    #by using recursive function we can extend it to any number of kSum  ---> time complexity O(k^3)
    #this can also be simulated using for-loops but recursive sol is more generic
    #when k == 2 during recusion we have reached base case i.e a sort of sub-problem two sum solved using two-pointers in a sorted array
    #we are not passing nums explicitly because it is accessible from enclosing namespace
    #however passing target although its accessible aswell b/c it keeps on changing as k decrements
    def kSum(k,start,target):
        #not base case  --> need to run for loops
        if k != 2:
            #len(nums) - k + 1 tells that we atleast need to have (k-1) values to select from remaining spots
            #e.g if k = 4 and len(nums) = 5 then we need to have atleast 3 values untouched for other iteration because values must be distinct
            for i in range(start,len(nums) - k + 1):
                #to avoid duplicates because using a repeated val will result in a repeated quadruplet
                if i > start and nums[i] == nums[i-1]:
                    continue 
                quad.append(nums[i])
                #recursive call
                kSum(k-1,i+1,target-nums[i])
                #to erase the just previously added number so that we can form other combinations aswell
                quad.pop()
            return
        #base case two sum II (two-pointers in sorted array)
        # l == r excluded because we want distinct indices
        #l starts from when there are two elements left to select from while two are already selected
        l , r = start , len(nums)-1
        while l < r:
            if nums[l] + nums[r] < target:
                l += 1
            elif nums[l] + nums[r] > target:    
                r -= 1
            else:
                #finally a quadruplet forms
                res.append(quad + [nums[l],nums[r]])    
                l += 1
                #to avoid duplicates because using a repeated val will result in a repeated quadruplet
                #we are potentially looking for more than 1 pair that could sum up to target
                while l < r and nums[l] == nums[l-1]:
                    l += 1
    kSum(4,0,target)
    return res                

print(fourSum([1, 0, -1, 0, -2, 2],0)) # [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]


