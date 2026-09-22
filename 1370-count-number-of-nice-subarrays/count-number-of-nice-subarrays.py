class Solution:
    def numberOfSubarrays(self, nums, k):
        prefix_map = {0: 1}
        curr_prefix = 0
        count = 0

        for num in nums:
            # Odd = 1, Even = 0
            curr_prefix += num % 2

            # Need previous prefix = curr_prefix - k
            count += prefix_map.get(curr_prefix - k, 0)

            # Store current prefix
            prefix_map[curr_prefix] = prefix_map.get(curr_prefix, 0) + 1

        return count
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        