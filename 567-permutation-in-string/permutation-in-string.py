class Solution:
    def checkInclusion(self, s1, s2):

        if len(s1) > len(s2):
            return False

        count1 = [0] * 26
        count2 = [0] * 26

        # frequency of s1
        for ch in s1:
            count1[ord(ch) - ord('a')] += 1

        # first window
        for i in range(len(s1)):
            count2[ord(s2[i]) - ord('a')] += 1

        if count1 == count2:
            return True

        # sliding window
        for right in range(len(s1), len(s2)):

            # add new character
            count2[ord(s2[right]) - ord('a')] += 1

            # remove old character
            left = right - len(s1)
            count2[ord(s2[left]) - ord('a')] -= 1

            if count1 == count2:
                return True

        return False
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        