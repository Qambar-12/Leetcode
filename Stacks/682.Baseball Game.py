class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        #Sum = 0
        for op in range(len(operations)):
            if stack:
                if operations[op] == 'D':
                    stack.append(int(stack[-1])*2)
                    #Sum += (int(stack[-1])*2)
                elif operations[op] == 'C':
                    stack.pop()
                    #Sum -= int(stack[-1])
                elif len(stack) >= 2 and operations[op] == '+':
                    stack.append(int(stack[-1])+int(stack[-2]))
                    #Sum += int(stack[-1])+int(stack[-2])       
                else:
                    stack.append(int(operations[op]))
                    #Sum += int(operations[op])
            else:
                stack.append(int(operations[op]))
                #Sum += int(operations[op])
        return sum(stack)                     
