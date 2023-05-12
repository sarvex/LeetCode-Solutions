# Time:  O(n)
# Space: O(1)

class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        return int(len(s) and s[-1] != ' ') + sum(
            1 for i in xrange(1, len(s)) if s[i] == ' ' and s[i - 1] != ' '
        )

    def countSegments2(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len([i for i in s.strip().split(' ') if i])

