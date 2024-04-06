class Solution:
    def simplifyPath(self, path: str) -> str:
        canonical = path.split('/')
        stack = []
        
        for val in canonical:
            #if val is '..' we need to move a level up in directory by popping most recent val from stack
            if val == '..':
                if stack: stack.pop()
            #if val is '.' or an empty string after splitting we must ignore it
            elif val == '.' or not val:
                continue
            else:
                stack.append(val)

        #using delimiter '/' to join string values and a leading forward slash is always part of simplified path
        return '/' + '/'.join(stack)  
