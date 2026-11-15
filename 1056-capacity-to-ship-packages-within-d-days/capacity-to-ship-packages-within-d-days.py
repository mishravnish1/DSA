class Solution(object):
    def shipWithinDays(self, weights, days):
        l, r = max(weights), sum(weights)
        res = r

        def canship(cap):
            ships = 1
            currcap = cap

            for w in weights:
                if currcap < w:
                    ships += 1
                    currcap = cap

                currcap -= w

            return ships <= days

        while l <= r:
            cap = (l + r) // 2

            if canship(cap):
                res = min(res, cap)
                r = cap - 1
            else:
                l = cap + 1

        return res                     
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        