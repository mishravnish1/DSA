class Solution:
    def numSubarraysWithSum(self, nums, goal):
        prefix_map = {0: 1}
        prefix_sum = 0
        count = 0

        for num in nums:
            prefix_sum += num

            required = prefix_sum - goal

            if required in prefix_map:
                count += prefix_map[required]

            prefix_map[prefix_sum] = prefix_map.get(prefix_sum, 0) + 1

        return count

        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        