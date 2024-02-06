def validPalindrome(s):
    """The function uses two pointers method together with slicing technique and returns True or False respectively after deleting atmost one character"""
    if s == s[::-1]:
        return True
    else:
        L,R = 0 , len(s)-1
        while L < R:
            if s[L] != s[R]:
                left_ch_skip = s[L+1:R+1]
                right_ch_skip = s[L:R]
                return (left_ch_skip == left_ch_skip[::-1]) or (right_ch_skip == right_ch_skip[::-1])
            L += 1
            R -= 1
    return True        
print(validPalindrome("aba"))
