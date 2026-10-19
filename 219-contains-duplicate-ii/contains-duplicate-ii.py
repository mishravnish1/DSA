class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        
        last_seen = {}
        for i, num in enumerate(nums): #Enumerate humein har element ka 'index' aur uski 'value' dono ek sath deta hai
            if num in last_seen and i - last_seen[num] <= k:
                return True
            last_seen[num] = i # Agar number naya hai ya gap k se bada tha, toh uski nayi position store/update karein
        return False            
                

                   

        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        