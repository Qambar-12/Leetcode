def sherlockAndAnagrams(s):
    #importing factorial from math module
    from math import factorial as f  
    List = []
    checked = []
    total = 0
    #if no character is repeating
    if len(set(s)) == len(s):
        return total
    #making all possible substrings
    for i in range(len(s)):
        for j in range(len(s)):
            substring = s[i:j+1]
            #sorting them so anagrams can be detected easily and using join method to make them string again
            substring = ''.join(sorted(substring))
            #check ensures no empty(null) substring or of length same as string s is in the list when appended
            if substring != '' and len(substring) != len(s):
                List.append(substring)
    #This makes list more sorted on basis of characters in list 
    List = sorted(List)
    for substring in List:
        #checking occurence of a substring i.e an anagram must have more than one occurence
        occurence = List.count(substring)
        #if substring is already present in list checked then the condition is skipped
        if (occurence > 1) and (substring not in checked):
            #nCr combination formula using factorial
            total += (f(occurence))/(f(occurence-2)*2)
            checked.append(substring)    
    #since division return float type casting back to integer
    return int(total)

    
