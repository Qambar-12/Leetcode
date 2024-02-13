def digitCount(num):
    from collections import Counter
    #Create a hashMap of the digits with their frequency of occurence
    hashMap = Counter(num)
    for i , digit in enumerate(num):
        #Type cast the digit to int because the hashMap stores the frequency of digits as int
        if hashMap[str(i)] != int(digit):
            print(hashMap[str(i)],digit)
            return False
    return True        
print(digitCount("3110")) 