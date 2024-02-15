def dailyTemperatures(temperatures):
    answer = [0] * len(temperatures)
    stack = []  # this will store the index of the 'unresolved' temperatures

    for i in range(len(temperatures)):
        # while stack is not empty and the current temperature is greater than the last 'unresolved' one
        while stack and temperatures[i] > temperatures[stack[-1]]:
            last_unresolved_index = stack.pop()
            answer[last_unresolved_index] = i - last_unresolved_index
        stack.append(i)

    return answer
