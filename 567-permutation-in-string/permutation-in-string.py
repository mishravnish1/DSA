class Solution(object):
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2):
            return False

        count1 = {}
        count2 = {}
        k = len(s1)
        left = 0

        for ch in s1:
            count1[ch] = count1.get(ch, 0) + 1

        for i in range(k):
            ch = s2[i]
            count2[ch] = count2.get(ch, 0) + 1

        if count1 == count2:
            return True

        for right in range(k, len(s2)):
            count2[s2[left]] -= 1

            if count2[s2[left]] == 0:
                del count2[s2[left]]

            count2[s2[right]] = count2.get(s2[right], 0) + 1
            left += 1

            if count1 == count2:
                return True

        return False


        
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        