# Time:  O(logn)
# Space: O(logn)

class Solution(object):
    def confusingNumber(self, N):
        """
        :type N: int
        :rtype: bool
        """
        lookup = {"0":"0", "1":"1", "6":"9", "8":"8", "9":"6"}

        S = str(N)
        result = []
        for i in xrange(len(S)):
            if S[i] not in lookup:
                return False
        return any(S[i] != lookup[S[-(i+1)]] for i in xrange((len(S)+1)//2))
