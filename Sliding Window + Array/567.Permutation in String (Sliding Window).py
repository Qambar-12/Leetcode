def checkInclusion(s1, s2) :
        if len(s1) > len(s2):
            return False
        elif len(s1) == len(s2):
            if sorted(s1) == sorted(s2):
                return True
            else:
                return False
        else:
            from collections import Counter
            s1_dic = Counter(s1)
            i , j = 0 , len(s1)-1
            while j < len(s2):
                if i == 0:
                    window = s2[i:j+1]
                    window_dic = Counter(window)
                else:
                    window_dic[s2[i-1]] -= 1
                    if window_dic[s2[i-1]] == 0:
                        #we can use del method aswell
                        window_dic.pop(s2[i-1])
                    window_dic[s2[j]] += 1    
                if s1_dic == window_dic:
                    print(i,j)
                    return True
                else:
                    #Sliding window technique
                    i += 1
                    j += 1   
        return False                