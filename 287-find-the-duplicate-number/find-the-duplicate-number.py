class Solution:
    def findDuplicate(self, nums):

        slow=fast=0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        # Phase 2: Find cycle entrance
        slow2 = 0

        while True:
            slow=nums[slow]
            slow2=nums[slow2]
            if slow==slow2:
                return slow

   
        """
        :type nums: List[int]
        :rtype: int
        """
        