class Solution(object):
    def removeDigit(self, number, digit):
        last = -1
        for i in range(len(number)):
            if number[i] == digit:
                last = i
                if i + 1 < len(number) and number[i + 1] > digit:
                    return number[:i] + number[i + 1:]
        return number[:last] + number[last + 1:]
        """
        :type number: str
        :type digit: str
        :rtype: str
        """
        