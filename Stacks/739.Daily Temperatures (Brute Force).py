def dailyTemperatures(temperatures):
    if len(temperatures) == 1:
        return [0]
    if all(x == temperatures[0] for x in temperatures):
        return len(temperatures)*[0]
    if sorted(temperatures,reverse = True) == temperatures:
        return len(temperatures)*[0]
    else:   
        answer = len(temperatures)*[0]
        i,j = 0,1
        count = 1
        while True:
            if j == len(temperatures)-1:
                if i == len(temperatures)-2:
                    if temperatures[i] < temperatures[j]:
                        answer[i] = count
                    else:
                        answer[i] = 0
                    return answer
                else:
                    if temperatures[i] < temperatures[j]:
                        answer[i] = count
                        i += 1
                        j = i + 1
                        count = 1
                    else:
                        answer[i] = 0
                        i += 1
                        j = i + 1   
                        count = 1     
            else:
                if temperatures[i] < temperatures[j]:
                    answer[i] = count
                    i += 1
                    j = i + 1
                    count = 1
                else:
                    count += 1   
                    j += 1                
print(dailyTemperatures([30,40,50,60]))
