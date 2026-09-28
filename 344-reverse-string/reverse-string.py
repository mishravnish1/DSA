class Solution(object):
    def reverseString(self, s):
        result = []

        for i in range(len(s) - 1, -1, -1):
            result.append(s[i])

        s[:] = result

        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        