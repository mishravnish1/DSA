class Solution(object):
    def romanToInt(self, s):
        values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total, prev = 0, 0
        for ch in reversed(s):
            v = values[ch]
            total += v if v >= prev else -v
            prev = v
        return total
        """
        :type s: str
        :rtype: int
        """
        