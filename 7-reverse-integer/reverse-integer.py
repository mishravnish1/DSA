class Solution(object):
    def reverse(self, x):
        # 1. Agar number negative hai
        if x < 0:
            # Minus sign hatao, reverse karo, aur wapas minus lagao
            val = str(abs(x))
            rev = "-" + val[::-1]
            reversed_int = int(rev)
        else:
            # Agar positive hai toh seedha string banakar reverse karo
            val = str(x)
            rev = val[::-1]
            reversed_int = int(rev)
            
        # 2. LeetCode ki overflow condition (Yeh zaroori hai standard test cases ke liye)
        if reversed_int < -2**31 or reversed_int > 2**31 - 1:
            return 0
            
        return reversed_int

        """
        :type x: int
        :rtype: int
        """
        