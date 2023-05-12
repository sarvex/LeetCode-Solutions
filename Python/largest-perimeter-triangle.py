# Time:  O(nlogn)
# Space: O(1)

class Solution(object):
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort()
        return next(
            (
                A[i] + A[i + 1] + A[i + 2]
                for i in reversed(xrange(len(A) - 2))
                if A[i] + A[i + 1] > A[i + 2]
            ),
            0,
        )
