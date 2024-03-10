def lengthOfLastWord(s):
    #Alternate of python's builtin split function
    List = []
    ch = 0
    while ch < len(s):
        word = ''
        while ch < len(s) and s[ch] != ' ':
            word += s[ch]
            ch += 1
        List.append(word)
        ch += 1
    while List and List[-1] == '':
        List.pop()
    return len(List[-1])    
print(lengthOfLastWord(" abc de f g h     "))
#or simply use python's builtin split function
def lengthOfLastWord(s):
    return len(s.split()[-1])