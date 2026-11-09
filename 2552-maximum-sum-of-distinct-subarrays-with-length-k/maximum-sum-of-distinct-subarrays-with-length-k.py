class Solution(object):
    def maximumSubarraySum(self, nums, k):
        n = len(nums)
        left = 0
        curr_sum = 0
        seen = set()
        max_sum = 0

        for right in range(n):
            # If duplicate found, shrink window
            while nums[right] in seen:
                seen.remove(nums[left])
                curr_sum -= nums[left]
                left += 1
            
            # Add current element
            seen.add(nums[right])
            curr_sum += nums[right]

            # If window size == k
            if right - left + 1 == k:
                max_sum = max(max_sum, curr_sum)
                
                # Slide window
                seen.remove(nums[left])
                curr_sum -= nums[left]
                left += 1

        return max_sum
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        