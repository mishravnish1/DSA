class Solution(object):
    def merge(self, intervals):
        intervals.sort()
        result=[]
        current = intervals[0]
        for num in intervals[1:]:
            if num[0] <= current[1]:
                current[1] = max(current[1], num[1])
            else:
                result.append(current)
                current=num
        result.append(current)
        return result        

     
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        