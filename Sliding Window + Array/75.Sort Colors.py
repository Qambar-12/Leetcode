def sortColors(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    R,W,B =0,0,0
    for color in nums:
        if color == 0:
            R += 1
        elif color == 1:
            W += 1
        else:
            B += 1       
    nums[:R] = R*[0]
    nums[R:R+W] = W*[1]
    nums[R+W:] = B*[2]  
