# Time:  O(n)
# Space: O(1)

class Solution(object):
    def decode(self, encoded, first):
        """
        :type encoded: List[int]
        :type first: int
        :rtype: List[int]
        """
        result = [first]
        result.extend(result[-1]^x for x in encoded)
        return result
