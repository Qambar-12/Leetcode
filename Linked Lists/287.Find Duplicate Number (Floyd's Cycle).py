class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #there is guaranteed to be a duplicate b/c len(nums) == n + 1 and 1 <= nums[i] <= n
        
        #USING FAST AND SLOW POINTERS (FLOYD'S ALGORITHM)
        #intuition behind the code is that we can convert it a linked list having a cycle
        #for e.g 1 [0-->1] [1-->3] [3-->2] [2-->4] [4-->2] so there is a cycle starting from 2
        #first pass of algorithm where we find intersection of fast and slow pointer
        slow , fast  = 0 , 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        #this intersection point has equal distance from start of cycle as start of cycle has from start of list
        #second pass of algorithm so we assign a new pointer 
        #and the next intersection will give us start of cycle
        slow2 = 0        
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
