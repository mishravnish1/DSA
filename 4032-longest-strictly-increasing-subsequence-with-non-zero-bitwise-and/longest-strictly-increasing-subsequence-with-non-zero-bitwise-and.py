
from bisect import bisect_left

class Solution(object):
    def longestSubsequence(self, nums):

        def lis(arr):
            dp = []

            for num in arr:
                idx = bisect_left(dp, num)

                if idx == len(dp):
                    dp.append(num)
                else:
                    dp[idx] = num

            return len(dp)

        ans = 0

        for bit in range(max(nums).bit_length()):
            arr = []

            for num in nums:
                if num & (1 << bit):
                    arr.append(num)

            ans = max(ans, lis(arr))

        return ans

        """
        :type nums: List[int]
        :rtype: int
        """
        