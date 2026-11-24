class Solution(object):
    def removeDigit(self, number, digit):
        for i in range(len(number)):
            if number[i] == digit:
                if i + 1 < len(number) and number[i + 1] > digit:
                    return number[:i] + number[i+1:]

        i = number.rfind(digit)
        return number[:i] + number[i+1:]
        """
        :type number: str
        :type digit: str
        :rtype: str
        """
        