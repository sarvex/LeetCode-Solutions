# Time:  O(n)
# Space: O(1)

class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        return [i for i in xrange(-(n//2), n//2+1) if i != 0 or n%2 != 0]
