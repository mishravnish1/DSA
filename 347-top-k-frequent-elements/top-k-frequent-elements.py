class Solution(object):
    def topKFrequent(self, nums, k):
        # 1. Correctly initialize count as a dictionary
        count = {} 
        freq = [[] for i in range(len(nums) + 1)]
        
        # 2. Populate the frequency dictionary
        for n in nums:
            count[n] = 1 + count.get(n, 0)
            
        # 3. Use .items() instead of .item()
        for n, c in count.items(): 
            freq[c].append(n)
            
        res = []
        # 4. Iterate backward from highest frequency bucket
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                # 5. Fix logic bug by checking >= to avoid overshoot
                if len(res) >= k: 
                    return res   
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        