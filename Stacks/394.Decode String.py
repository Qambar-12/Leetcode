def decodeString(s):
        #decoded = ''
        stack = []
        for ch in s:
            if ch == ']':
                string = ''
                while True:
                    if stack[-1] == '[':
                        stack.pop()
                        digit = ''
                        while stack and stack[-1].isdigit():
                             digit += stack.pop()
                        digit = digit[::-1]     
                        string = int(digit) * string
                        #decoded += string[::-1]
                        stack.append(string[::-1])
                        break
                    else:
                        if len(stack[-1]) > 1:
                            string += stack.pop()[::-1]
                        else:
                            string += stack.pop()    
            else: 
                stack.append(ch)                     
        return ''.join(stack)      