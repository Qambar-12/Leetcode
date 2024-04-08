def findClosestElements(arr, k, x):
        l = 0
        r = len(arr)-1
        while r - l + 1 > k:
            # once it is k we have found the window
            if x - arr[l] <= arr[r] - x:
                r -= 1
            else:
                l += 1 
        return arr[l:r+1]
print(findClosestElements([1,2,3,4,5], 2, -1)) # [1,2,3,4]