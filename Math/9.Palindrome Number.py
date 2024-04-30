class Solution:
    # T = O(logn)
    def isPalindrome(self, x: int) -> bool:
        #  not converting into string
        if x < 0:
            return False

        res = 0
        orig = x
        while x != 0:
            res = res * 10 + x % 10
            x //= 10
        return res == orig
print(Solution().isPalindrome(121))  # True