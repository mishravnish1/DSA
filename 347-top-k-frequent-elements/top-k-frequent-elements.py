class Solution(object):
    def topKFrequent(self, nums, k):
        # 1. Correctly initialize count as a dictionary
        count = {}
        for x in nums:
            count[x] = count.get(x, 0) + 1

    # Step 2: frequency ko index bana ke buckets
        buckets = [[] for _ in range(len(nums) + 1)]
        for x, f in count.items():
            buckets[f].append(x)

    # Step 3: high frequency se low ki taraf padho
        res = []
        for f in range(len(buckets) - 1, 0, -1):
            for x in buckets[f]:
                res.append(x)
                if len(res) == k:
                    return res    
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        