class Solution:
    def isValid(self, s: str) -> bool:
        hashMap = {'(':')','{':'}','[':']'}
        #To check whether length of string is an odd number or not and starting value of string is not a closing bracket
        if len(s) % 2 != 0 or (s[0] in hashMap.values()):
            return False
        else:
            #Initializing an empty list named stack (LIFO : Last In First Out)
            stack = []
            #Traversing all elements of string
            for bracket in s:
                #if it is a opening bracket append it's closing bracket in the stack 
                if bracket in hashMap:
                    stack.append(hashMap[bracket])
                #if it is a closing bracket first check that the stack is not empty (if empty return False) and then compare it with Last In value if it matches continue the loop else return False
                else:
                    if stack:
                        if bracket == stack[-1]:
                            stack.pop()
                        else:
                            return False    
                    else:
                        return False
        #atlast checking that all pairs of brakcets have been accomodated so our stack must be empty
        if stack:
            return False
        else:
            return True                    



        
            
