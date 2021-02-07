class Solution:
    def isPalindrome_string(self, x: int) -> bool:
        if x < 0:
            return False
        if str(x) != str(x)[::-1]:
            return False
        else:
            return True

    # solution without string conversion
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        y, rev = x, 0
        while y > 0:
            rev = rev * 10 + y % 10
            y /= 10
        
        return rev == x
