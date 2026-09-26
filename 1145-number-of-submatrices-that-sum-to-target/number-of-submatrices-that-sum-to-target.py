class Solution:
    def numSubmatrixSumTarget(self, matrix, target):
        rows = len(matrix)
        cols = len(matrix[0])
        count = 0

        for top in range(rows):
            temp = [0] * cols

            for bottom in range(top, rows):

                # Compress rows into 1D array
                for col in range(cols):
                    temp[col] += matrix[bottom][col]

                # 1D Subarray Sum = target
                prefix = 0
                prefix_map = {0: 1}

                for num in temp:
                    prefix += num

                    if prefix - target in prefix_map:
                        count += prefix_map[prefix - target]

                    prefix_map[prefix] = prefix_map.get(prefix, 0) + 1

        return count
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: int
        """
        