class Solution(object):
    def maxSubArray(self, nums):
        maxi = float("-inf")
        total=0
        n=len(nums)

        for i in range(0,n):
            total = total + nums[i]
            maxi=max(maxi,total)
            if total <0:
                total=0

        return maxi