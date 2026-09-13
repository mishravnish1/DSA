class Solution(object):
    def maxVowels(self, s, k):
        left=0
        window_sum=0
        max_vowels = 0
        for right in range(len(s)):
            if s[right] in "aeiou":
                window_sum += 1
            if right-left +1==k:
                max_vowels=max(max_vowels,window_sum)
                if s[left] in "aeiou":
                    window_sum -= 1
                left+=1
        return max_vowels      
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        