class Solution:
    def findAnagrams(self, s, p):
        if len(p)>len(s):
            return[]

        count_p=[0]*26
        count_s=[0]*26

        for ch in p:
            count_p[ord(ch)-ord('a')]+=1
        for i in range(len(p)):
            count_s[ord(s[i])-ord('a')]+=1
        result = []
        left = 0

        if count_p == count_s:
            result.append(0)

        for right in range(len(p), len(s)):

            count_s[ord(s[right]) - ord('a')] += 1
            count_s[ord(s[left]) - ord('a')] -= 1

            left += 1

            if count_p == count_s:
                result.append(left)

        return result       

                

            


   

        
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        