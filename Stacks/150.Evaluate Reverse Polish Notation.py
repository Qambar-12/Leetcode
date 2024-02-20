def evalRPN(tokens):
    stack =[]
    operators = {'+','-','*','/'}
    if len(tokens) == 1:
        return int(tokens[0])
    for i in tokens:
        if (stack) and (i in operators) and (len(stack) >= 2):
            operand1 = stack.pop()
            operand2 = stack.pop()
            result = eval(str(operand2) + i + str(operand1))
            print(result)
            stack.append(int(result))
        else:
            stack.append(i)
    print(stack)            
    return int(result)           
print(evalRPN(["0","3","/"])) 
