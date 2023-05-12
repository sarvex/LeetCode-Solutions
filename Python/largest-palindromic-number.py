# Time:  O(n)
# Space: O(1)

import collections


# freq table, greedy
class Solution(object):
    def largestPalindromic(self, num):
        """
        :type num: str
        :rtype: str
        """
        cnt = collections.Counter(num)
        result = []
        for i in reversed(xrange(10)):
            if not cnt[str(i)]//2 or (i == 0 and not result):
                continue
            result.extend(str(i) for _ in xrange(cnt[str(i)]//2))
        result.append(max([k for k, v in cnt.iteritems() if v%2] or [""]))
        result.extend(result[i] for i in reversed(xrange(len(result)-1)))
        return "".join(result) or "0"
