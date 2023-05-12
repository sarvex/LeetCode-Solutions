# Time:  O(n^2)
# Space: O(n)

class Solution(object):
    def countTriples(self, n):
        """
        :type n: int
        :rtype: int
        """
        lookup = {i**2 for i in xrange(1, n+1)}
        result = 0
        for i in xrange(1, n+1):
            for j in xrange(1, n+1):
                result += int(i**2+j**2 in lookup)
        return result
