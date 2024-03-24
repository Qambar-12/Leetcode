def singleNonDuplicate(nums):
    l,r = 0,len(nums)-1
    while l <= r:
        mid = (l+r)//2
        if mid == 0 or mid == len(nums)-1:
            return nums[mid]
        else:
            if nums[mid-1] == nums[mid]:
                if (mid-2-l+1) % 2 :
                    r = mid-2
                else:
                    l = mid+1
            elif nums[mid+1] == nums[mid] :
                if (r-(mid+2)+1) % 2:
                    l = mid+2
                else:
                    r = mid-1
            else:
                return nums[mid]  
print(singleNonDuplicate([1,1,2]))                      