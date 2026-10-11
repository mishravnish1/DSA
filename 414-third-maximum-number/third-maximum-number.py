class Solution(object):
    def thirdMax(self, nums):
        # Sirf unique numbers rakhein aur descending order me sort karein
        unique_nums = sorted(list(set(nums)), reverse=True)
        
        # Agar 3 ya usse zyada unique elements hain toh 3rd return karein
        if len(unique_nums) >= 3:
            return unique_nums[2]
        
        # Warna sabse bada element return karein
        return unique_nums[0]


        """
        :type nums: List[int]
        :rtype: int
        """
        