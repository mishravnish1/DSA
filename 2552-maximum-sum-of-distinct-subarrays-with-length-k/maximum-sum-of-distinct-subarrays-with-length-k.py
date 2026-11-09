class Solution(object):
    def maximumSubarraySum(self, nums, k):
        seen = set()
        curr_sum=0
        max_sum=0
        left=0
        for r in range(len(nums)):
            while nums[r] in seen:
                seen.remove(nums[left])
                curr_sum-=nums[left]
                left+=1
            seen.add(nums[r])
            curr_sum += nums[r]
            if r-left+1==k:
                max_sum=max(max_sum,curr_sum)
                seen.remove(nums[left])
                curr_sum -= nums[left]
                left += 1

        return max_sum
    


        



            

        
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        