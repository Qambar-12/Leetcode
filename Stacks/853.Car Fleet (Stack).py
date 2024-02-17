def carFleet(target,position,speed):
    stack =[]
    d = {}
    #Creating a hashmap or alternateky using zip function
    for i in range(len(position)):
        d[position[i]] = i     
    position.sort()
    for i,e in enumerate(position):
        while stack and (stack[-1] > speed[d[e]]) :
            t =  (e-position[i-1]) / (stack[-1] - speed[d[e]])
            #meet_position = e + t * speed[d[e]] (Equivalent)
            meet_position = position[i-1] + (t * stack[-1])  #meeting position of the car in front
            if meet_position <= target:
               stack.pop()
            break       
        stack.append(speed[d[e]]) 
    return len(stack)    
print(carFleet(100,[1,3,5,7,9],[10,20,30,40,50]))
