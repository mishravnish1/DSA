class Solution:
    def secondHighest(self, s):
        largest = -1
        second_largest = -1
        
        for char in s:
            if char.isdigit():
                d = int(char)
                
                if d > largest:
                    second_largest = largest
                    largest = d
                elif second_largest < d < largest:
                    second_largest = d
                    
        return second_largest

        """
        :type s: str
        :rtype: int
        """
        