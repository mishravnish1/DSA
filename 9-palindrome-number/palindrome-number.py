class Solution(object):
    def isPalindrome(self, x):
        
        s = str(x)
        reversed_s = s[::-1]

        return s == reversed_s   
        """
        :type x: int
        :rtype: bool
        """
        