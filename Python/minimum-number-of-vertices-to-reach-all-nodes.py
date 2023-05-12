# Time:  O(e)
# Space: O(n)

class Solution(object):
    def findSmallestSetOfVertices(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        lookup = {v for u, v in edges}
        return [i for i in xrange(n) if i not in lookup]
