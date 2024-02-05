def isPalindrome(s):
      s = s.lower()
      for ch in s:
          if not(ch.isalnum()):
              s = s.replace(ch,'')
      return s == s[::-1]           

