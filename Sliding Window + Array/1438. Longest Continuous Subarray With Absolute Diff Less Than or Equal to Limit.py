class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        #the subarray is valid as long as max-min <= limit
        #when the window is not valid any more we shift our left pointer
        #but how do we know our curMax and currMin again for new window

        #so we can maintain some sort of order while adding elements to some data structure
        #HEAP or QUEUE
        min_q = deque() #monotonic increasing order  
        max_q = deque() #monotonic decreasing order 

        l = 0
        res = 0
        for r in range(len(nums)):
            #to maintain monotonic increasing order
            while min_q and nums[r] < min_q[-1]:
                min_q.pop()
            #to maintain monotonic decreasing order    
            while max_q and nums[r] > max_q[-1]:
                max_q.pop()  

            min_q.append(nums[r])
            max_q.append(nums[r])

            #validate whether max_q[0] - min_q[0] > limit
            while max_q[0] - min_q[0] > limit:
                if nums[l] == min_q[0]:
                    min_q.popleft()
                if nums[l] == max_q[0]:
                    max_q.popleft()    
                l += 1

            res = max(res, r-l+1)
        return res    

