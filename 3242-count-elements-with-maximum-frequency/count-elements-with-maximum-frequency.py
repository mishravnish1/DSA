class Solution(object):
    def maxFrequencyElements(self, nums):
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        max_freq = max(freq.values())

        total = 0
        for count in freq.values():
            if count == max_freq:
                total += count

        return total

        """
        :type nums: List[int]
        :rtype: int
        """
        