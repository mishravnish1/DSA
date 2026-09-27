class Solution(object):
    def insert(self, intervals, newInterval):
        res=[]
        for current in intervals:
            if current[1] < newInterval[0]:
                res.append(current)
            elif current[0] <= newInterval[1]:
                newInterval[0] = min(current[0], newInterval[0])
                newInterval[1] = max(current[1], newInterval[1])
            else:
                res.append(newInterval)
                newInterval = current 
        res.append(newInterval)

            

        return res
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        