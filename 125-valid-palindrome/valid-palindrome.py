class Solution(object):
    def isPalindrome(self, s):
        cleaned=""
        for char in s:
            if char.isalnum():
                cleaned += char.lower()
        reversed_s = cleaned[::-1]
        return cleaned == reversed_s


                  
        