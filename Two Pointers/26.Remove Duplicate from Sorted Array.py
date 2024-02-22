def removeDuplicates(nums):
    if len(nums) == 1:
        return 1
    else:
        #Two-pointer approach
        k = 1
        i , j = 0,1
        while i < len(nums)-1 and nums[j] != '_':
            if nums[i] == nums[j]:
                nums.pop(j)
                nums.append('_')
            else:
                k += 1
                i = j
                j += 1
        nums = nums[:k]        
        print(nums)
        return k        