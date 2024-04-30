class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_ = set(nums)     #because lookup in set is O(1) time complexity
        longest = 0
        #we need to iterate through the entire array and check whether a number is start of sequence i.e must not have any left neighbour in set_
        for n in nums:
            #i.e n is the start of a sequence
            length = 1
            if n-1 not in set_:
                while (n+length) in set_:
                    length += 1
            longest = max(longest,length)
        return longest
