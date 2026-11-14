class Solution(object):
    def minEatingSpeed(self, piles, h):
        left = 1
        right = max(piles)
        ans = right

        while left <= right:
            mid = (left + right) // 2

            total_hours = 0

            for pile in piles:
                total_hours += (pile + mid - 1) // mid

            if total_hours <= h:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        