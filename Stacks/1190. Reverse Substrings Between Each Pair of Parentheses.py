class Solution:
    def reverseParentheses(self, s: str) -> str:
        #standard stack algorithm
        stack = []
        for ch in s:
            if ch != ')':
                stack.append(ch)
            else:
                temp = []
                while stack:
                    if stack[-1] == '(':
                        stack.pop()
                        break   
                    else:
                        temp.append(stack.pop())     
                stack += temp            
        return ''.join(stack)