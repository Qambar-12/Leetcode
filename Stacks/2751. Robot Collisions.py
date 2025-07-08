class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        #creating a mapping before sorting positions 
        pos_map = {p:i for i,p in enumerate(positions)}

        #observations:
        #1.) if some initial robots are moving to left they would never collide
        #2.)speed is irrelevant in this context
        #3.)collision occurs when robot at left moving to right and vice versa
        #WHILE LOOP
        #4.)we need to continue popping from stack as long as the robot at TOS fulfills condition of collision with incoming robot we are traversing after sorting positions
        #5.)if a robot is moving to right it wont collide with anything to its left so we can directly append to stack


        stack = []   #index
        for p in sorted(positions):
            i = pos_map[p]
            if directions[i] == "R":
                stack.append(i)
            else:
                while stack and directions[stack[-1]] == "R" and healths[i]:
                    j = stack.pop()
                    if healths[i] == healths[j]:
                        healths[i]= healths[j] = 0
                    elif healths[i] > healths[j]:
                        healths[j] = 0
                        healths[i] -= 1
                    else:
                        healths[i] = 0
                        healths[j] -= 1
                        stack.append(j)
                if healths[i]:
                    stack.append(i)
        return [h for h in healths if h > 0]                    
        
                    
