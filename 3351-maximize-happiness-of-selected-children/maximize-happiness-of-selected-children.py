class Solution(object):
    def maximumHappinessSum(self, happiness, k):
        happiness.sort(reverse=True)

        total = 0

        for i in range(k):
            total += max(0, happiness[i] - i)

        return total
        """
        :type happiness: List[int]
        :type k: int
        :rtype: int
        """
        