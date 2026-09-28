class Solution(object):
    def isPalindrome(self, s):
        cleaned=""
        #empty string
        for char in s:
            if char.isalnum(): #if char is alnum so clean it make it in lower case
                cleaned += char.lower()
        reversed_s = cleaned[::-1] #make one reverse 
        return cleaned == reversed_s #compare 


                  
        