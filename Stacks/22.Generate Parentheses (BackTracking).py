def generateParenthesis(n):
    stack = []
    res = []

    # openN: number of open parenthesis
    # closedN: number of closed parenthesis
    #using backtracking to generate all possible combinations
    # if openN < n, add "("
    # if closedN < openN, add ")"
    #if openN == closedN == n, add the combination to res
    #stack.pop() to backtrack to the previous state i.e remove the last added parenthesis and try the other option
    #return statement basically helps to pop out of the recursive call address and to its previous state/caller
    def backtrack(openN, closedN):
        if openN == closedN == n:
            res.append("".join(stack))
            return

        if openN < n:
            stack.append("(")
            backtrack(openN + 1, closedN)
            stack.pop()
        if closedN < openN:
            stack.append(")")
            backtrack(openN, closedN + 1)
            stack.pop()

    backtrack(0, 0)
    return res
print(generateParenthesis(3))  # ["((()))","(()())","(())()","()(())","()()()"]