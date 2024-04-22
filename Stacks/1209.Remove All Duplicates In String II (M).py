class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []     #[ch,count]
        for ch in s:
            if stack and stack[-1][0] == ch:
                stack[-1][1] += 1
            #it means that stack is empty or ch is not duplicate
            #so we need to append to stack with count 1
            else:
                stack.append([ch,1])
            if stack[-1][1] == k:
                stack.pop()

        res = ''
        for ch , count in stack:
            res += (ch * count)
        return res                
                    
                    
