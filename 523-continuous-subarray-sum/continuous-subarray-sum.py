class Solution:
    def checkSubarraySum(self, nums, k):

        remainder_map = {0: -1}
        prefix = 0

        for i, num in enumerate(nums):

            prefix += num
            remainder = prefix % k

            if remainder in remainder_map:
                if i - remainder_map[remainder] >= 2:
                    return True
            else:
                remainder_map[remainder] = i

        return False                  


           
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        