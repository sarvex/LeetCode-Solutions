# Time:  O(n)
# Space: O(1)

class Solution(object):
    lookup = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}

    # @param {string} num
    # @return {boolean}
    def isStrobogrammatic(self, num):
        n = len(num)
        return not any(
            num[n - 1 - i] not in self.lookup
            or num[i] != self.lookup[num[n - 1 - i]]
            for i in xrange((n + 1) / 2)
        )

