class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        #we will iterate over integer array nums looking for candidate k
        #we would be maintaining our 2D stack (monotonic decreasing) 
        #b/c there we would be looking at first element which must be nums[j] i.e greater than nums[k]
        #and the second element is the minimum to the left which must be as small as possible
        #and if any value fits in b/w these two elements in stack we have found out our sol

        
        #a subsequence means the order must remain same but it is not necassirily contigous
        stack = []          #[[n , minLeft]]
        currMin = nums[0]
        if len(nums) >= 3:
            #because our first element can never be candidate for k index
            for n in nums[1:] :
                #continue popping while the values for j on stack are less than k
                while stack and n >= stack[-1][0]:
                    stack.pop()
                #when the loop terminates either stack is empty or we have found a j value for which is greater than k val
                #now checking whether that is k value is greater than i val i.e the minLeft to fulfill inequality condition
                if stack and n > stack[-1][1]:
                    return True

                stack.append([n , currMin])
                #update the currMin 
                currMin = min(currMin, n)
        return False               
