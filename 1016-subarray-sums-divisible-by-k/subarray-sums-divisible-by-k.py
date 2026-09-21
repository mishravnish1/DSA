class Solution:
    def subarraysDivByK(self, nums, k):
        freq = {0: 1}
        prefix = 0
        count = 0

        for num in nums:
            prefix += num

            rem = prefix % k

            if rem in freq:
                count += freq[rem]

            freq[rem] = freq.get(rem, 0) + 1

        return count
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        