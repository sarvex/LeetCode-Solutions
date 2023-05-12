# Time:  O(nlogn)
# Space: O(n)

import collections


class Solution(object):
    # @param {string[]} strings
    # @return {string[][]}
    def groupStrings(self, strings):
        groups = collections.defaultdict(list)
        for s in strings:  # Grouping.
            groups[self.hashStr(s)].append(s)

        return [sorted(val) for key, val in groups.iteritems()]

    def hashStr(self, s):
        base = ord(s[0])
        return "".join(
            unichr(ord('a') + ord(s[i]) - base)
            if ord(s[i]) - base >= 0
            else unichr(ord('a') + ord(s[i]) - base + 26)
            for i in xrange(len(s))
        )

