class Solution(object):
    def findMaxAverage(self, nums, k):

        window_sum = 0

        # First window
        for i in range(k):
            window_sum += nums[i]

        maximum = window_sum

        # Slide window
        for right in range(k, len(nums)):

            window_sum += nums[right]
            window_sum -= nums[right - k]

            maximum = max(maximum, window_sum)

        return maximum / float(k)
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        