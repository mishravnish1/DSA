from bisect import bisect_left, insort

class Solution:
    def maxSumSubmatrix(self, matrix, k):
        rows = len(matrix)
        cols = len(matrix[0])

        ans = float("-inf")

        # Make columns the smaller dimension
        if rows > cols:
            matrix = [list(row) for row in zip(*matrix)]
            rows, cols = cols, rows

        for left in range(cols):
            row_sum = [0] * rows

            for right in range(left, cols):
                # Compress columns left -> right into 1D array
                for r in range(rows):
                    row_sum[r] += matrix[r][right]

                # Find max subarray sum <= k
                prefix = 0
                sorted_prefix = [0]

                for x in row_sum:
                    prefix += x

                    # Need previous prefix >= prefix - k
                    idx = bisect_left(sorted_prefix, prefix - k)

                    if idx < len(sorted_prefix):
                        ans = max(ans, prefix - sorted_prefix[idx])

                    insort(sorted_prefix, prefix)

                    if ans == k:
                        return ans

        return ans
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        