class Solution(object):
    def thirdMax(self, nums):
        largest = None
        second_largest = None
        third_largest = None

        for num in nums:
            # Duplicate elements ko ignore karne ke liye
            if num == largest or num == second_largest or num == third_largest:
                continue
            
            # Case 1: Naya largest mil gaya
            if largest is None or num > largest:
                third_largest = second_largest
                second_largest = largest
                largest = num
            
            # Case 2: Largest se chota par second_largest se bada
            elif second_largest is None or num > second_largest:
                third_largest = second_largest
                second_largest = num
            
            # Case 3: Second_largest se chota par third_largest se bada
            elif third_largest is None or num > third_largest:
                third_largest = num

        # Agar third_largest nahi mila (matlab < 3 distinct numbers hain), 
        # toh rule ke mutabik max (largest) return karein.
        return third_largest if third_largest is not None else largest

        """
        :type nums: List[int]
        :rtype: int
        """
        