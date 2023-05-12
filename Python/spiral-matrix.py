# Time:  O(m * n)
# Space: O(1)

class Solution(object):
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        result = []
        if matrix == []:
            return result

        left, right, top, bottom = 0, len(matrix[0]) - 1, 0, len(matrix) - 1

        while left <= right and top <= bottom:
            result.extend(matrix[top][j] for j in xrange(left, right + 1))
            result.extend(matrix[i][right] for i in xrange(top + 1, bottom))
            result.extend(
                matrix[bottom][j]
                for j in reversed(xrange(left, right + 1))
                if top < bottom
            )
            result.extend(
                matrix[i][left]
                for i in reversed(xrange(top + 1, bottom))
                if left < right
            )
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1

        return result


