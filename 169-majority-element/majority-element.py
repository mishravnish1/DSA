class Solution(object):
    def majorityElement(self, nums):
        n = len(nums)
        count=0
        el=0
        for num in nums:
            if count==0:
                count=1
                el=num
            elif el==num:
                count+=1
            else:
                count-=1
        count1=nums.count(el)
        if count1 > (n // 2):
            return el
        return -1            
                
        
        """ Iterate through the map to
        find the majority element"""
        for num, count in mp.items():
            if count > n // 2:
                return num
        
        # Return -1 if no majority element is found
        return -1
       
                  

        """
        :type nums: List[int]
        :rtype: int
        """
        