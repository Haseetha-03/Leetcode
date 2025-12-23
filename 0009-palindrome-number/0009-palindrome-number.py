class Solution:
    def isPalindrome(self, x: int) -> bool:
        x1=str(x)
        rev=x1[::-1]
        if x1==rev:
            return True
        else:
            return False