def trap(height):
        #for each bar the water it can trap is given by: min(maxL,maxR) - height[i]
        #we can you two pointers at ends of array to compute maxLeft and maxRight variable values
        #at endpoints since there is no boundary on other side it cant trap any water
        if not height : return 0
        trapWater = 0
        l , r = 0 , len(height)-1
        leftMax , rightMax = height[l] , height[r]
        #using two-pointer approach to optimize memory 
        while l < r :
            #althought rightmax may not be true rightMax but since leftMax is still smaller we are not concerned with that
            if leftMax <= rightMax:
                diff = (leftMax) - height[l]
                if diff > 0:
                    trapWater += diff
                l += 1
                leftMax = max(leftMax,height[l])
            else:
                diff = (rightMax) - height[r] 
                if diff > 0:
                    trapWater += diff
                r -= 1
                rightMax = max(rightMax,height[r])    
        return trapWater    
print(trap([0,1,0,2,1,0,1,3,2,1,2,1])) #6