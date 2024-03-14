def removeDuplicates(nums):
    k,i,currCount = 0 , 0 ,0
    curr = nums[0]
    while i < len(nums) and nums[i] != None:
        if nums[i] == curr:
            if currCount < 2:
                currCount += 1
                k += 1
                i += 1
            else:
                nums.pop(i)
                nums.append(None)
        else:
            curr = nums[i]
            currCount = 1
            k += 1
            i += 1           
    return k,nums
print(removeDuplicates([0,0,1,1,1,1,2,3,3]))