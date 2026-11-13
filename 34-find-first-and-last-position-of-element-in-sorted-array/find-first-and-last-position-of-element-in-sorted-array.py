class Solution(object):
    def searchRange(self, nums, target):
        first = self.firstOccurrence(nums, target)
        last = self.lastOccurrence(nums, target)
        return [first, last]

    def firstOccurrence(self, nums, target):
        left, right = 0, len(nums) - 1
        ans = -1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                ans = mid
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return ans

    def lastOccurrence(self, nums, target):
        left, right = 0, len(nums) - 1
        ans = -1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                ans = mid
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return ans
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        