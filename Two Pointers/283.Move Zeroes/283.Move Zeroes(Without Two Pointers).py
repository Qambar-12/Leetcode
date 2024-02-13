def moveZeroes(nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroes = nums.count(0)
        i = 0
        nums += ([0]*zeroes)
        while i < zeroes:
            nums.remove(0)
            i +=1                 
        return nums 
