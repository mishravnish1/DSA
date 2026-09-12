from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):

        dq = deque()
        result = []

        for right in range(len(nums)):

            # Window ke bahar wale index ko remove
            if dq and dq[0] < right - k + 1:
                dq.popleft()

            # Chhoti values ko remove
            while dq and nums[dq[-1]] < nums[right]:
                dq.pop()

            dq.append(right)

            # Window complete hai
            if right >= k - 1:
                result.append(nums[dq[0]])

        return result
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        