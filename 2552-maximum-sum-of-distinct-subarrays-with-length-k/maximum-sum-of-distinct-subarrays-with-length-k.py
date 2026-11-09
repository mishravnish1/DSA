class Solution(object):
    def maximumSubarraySum(self, nums, k):
        n = len(nums)

        if k <= 0 or n < k:
            return 0

        window_sum = 0
        seen = {}
        max_sum = 0

        # Build first window
        for i in range(k):
            window_sum += nums[i]
            seen[nums[i]] = seen.get(nums[i], 0) + 1

        if len(seen) == k:
            max_sum = window_sum

        # Slide the window
        for i in range(k, n):
            window_sum += nums[i]
            seen[nums[i]] = seen.get(nums[i], 0) + 1

            window_sum -= nums[i-k]
            seen[nums[i-k]] -= 1

            if seen[nums[i-k]] == 0:
                del seen[nums[i-k]]

            if len(seen) == k:
                max_sum = max(max_sum, window_sum)

        return max_sum


            

        
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        