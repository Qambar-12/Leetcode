class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        mapping_operand = {'f':False,'t':True}
        mapping_operator = {'!':'not','&':'and','|':'or'}
        expression = expression.replace(",","")
        stackOperators = []
        stackOperands = []
        for ch in expression:
            if ch in mapping_operand:
                stackOperands.append(mapping_operand[ch])
            elif ch in mapping_operator:
                stackOperators.append(mapping_operator[ch])
            elif ch == '(':
                stackOperands.append('(')
            else:
                temp = []
                while stackOperands[-1] != "(":
                    temp.append(stackOperands.pop())
                stackOperands.pop()    
                operator = stackOperators.pop()
                if len(temp) == 1: 
                    if operator == 'not':
                        stackOperands.append(not temp[0])
                    else:
                        stackOperands.append(temp[0])
                else:
                    if operator == 'and':
                        if (False in temp):
                            stackOperands.append(False)
                        else:
                            stackOperands.append(True)
                    else:
                        if (True in temp):
                            stackOperands.append(True)
                        else:
                            stackOperands.append(False)
        return stackOperands[-1]    


