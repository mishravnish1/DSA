class Solution:
    def findMaxLength(self, nums):
        first_seen = {0: -1}

        prefix_sum = 0
        max_len = 0

        for i, num in enumerate(nums):

            if num == 0:
                prefix_sum -= 1
            else:
                prefix_sum += 1

            if prefix_sum in first_seen:
                length = i - first_seen[prefix_sum]
                max_len = max(max_len, length)
            else:
                first_seen[prefix_sum] = i

        return max_len                        

        """
        :type nums: List[int]
        :rtype: int
        """
        