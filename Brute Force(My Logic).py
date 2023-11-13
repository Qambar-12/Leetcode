s = "xyzdcbb"
length = 0
for index in range(len(s)):
    for char in range(1,len(s)+1):
        subStr = s[index:char]     
        print(subStr)
        subStr_set = set(subStr)
        if len(subStr) != len(subStr_set):
            pass
        else :
            length = max(length,len(subStr))
print("The length of longest sub-string without repeating characters is",length)            
