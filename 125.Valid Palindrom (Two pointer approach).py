def isPalindrome(s):
    """The above function uses two pointer approach"""
    s = s.lower()
    for ch in s:
        if not(ch.isalnum()):
            s = s.replace(ch,'')
    #initialing the pointers used with extreme indices
    i = 0
    j = len(s)-1
    while i <= j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True
