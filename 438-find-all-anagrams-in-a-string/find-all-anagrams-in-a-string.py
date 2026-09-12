class Solution:
    def findAnagrams(self, s, p):

        if len(p) > len(s):
            return []

        count_p = [0] * 26
        count_s = [0] * 26

        # Frequency of p
        for ch in p:
            count_p[ord(ch) - ord('a')] += 1

        # First window
        for i in range(len(p)):
            count_s[ord(s[i]) - ord('a')] += 1

        result = []

        if count_p == count_s:
            result.append(0)

        # Sliding window
        for right in range(len(p), len(s)):

            # Add new character
            count_s[ord(s[right]) - ord('a')] += 1

            # Remove old character
            left = right - len(p)
            count_s[ord(s[left]) - ord('a')] -= 1

            # Check anagram
            if count_p == count_s:
                result.append(left + 1)

        return result
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        