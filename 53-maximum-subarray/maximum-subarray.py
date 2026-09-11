class Solution(object):
    def maxSubArray(self, nums):
        maxi = float("-inf")
        total = 0

        for num in nums:
            total += num
            maxi = max(maxi, total)
            if total < 0:
                total = 0

        return maxi