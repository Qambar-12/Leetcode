def removeElement(nums, val):
    length = len(nums)
    i , j = 0,len(nums)-1
    while i <= j and nums[i] != '_' and nums[j] != '_':
        if nums[i] == val:
            if nums[j] == val:
                nums[j] = '_'
                length -= 1
                j -= 1
            else:
                nums[i] = nums[j]
                nums[j] = '_'
                length -= 1
                i += 1
                j -= 1
        else:
            if nums[j] == val:
                nums[j] = '_'
                length -= 1    
                i += 1
                j -= 1
            else:
                i += 1                     
    return length                         
print(removeElement(([2,2,2,2,2],2)))