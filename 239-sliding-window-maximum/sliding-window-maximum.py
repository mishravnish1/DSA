from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):

        dq = deque()
        result = []
        left = 0

        for right in range(len(nums)):

            while dq and nums[dq[-1]] < nums[right]:
                dq.pop()

            dq.append(right)

            if right - left + 1 > k:
                left += 1

            if dq[0] < left:
                dq.popleft()

            if right - left + 1 == k:
                result.append(nums[dq[0]])

        return result
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        