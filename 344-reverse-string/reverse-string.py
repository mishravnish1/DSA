class Solution(object):
    def reverseString(self, s):
        result = []

        for i in range(len(s) - 1, -1, -1):
            result.append(s[i])

        for i in range(len(s)):
            s[i] = result[i]
        

        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        
        

        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        