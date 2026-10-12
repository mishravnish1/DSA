class Solution(object):
    def containsDuplicate(self, nums):
        seen={}

        for n in nums:
            if n in seen:
                return True
            seen[n]=nums
        return False    
        """
        :type nums: List[int]
        :rtype: bool
        """
        