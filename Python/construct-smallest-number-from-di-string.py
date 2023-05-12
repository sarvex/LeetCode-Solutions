# Time:  O(n)
# Space: O(1)

# constructive algorithms
class Solution(object):
    def smallestNumber(self, pattern):
        """
        :type pattern: str
        :rtype: str
        """
        result = []
        for i in xrange(len(pattern)+1):
            if i != len(pattern) and pattern[i] != 'I':
                continue
            result.extend(iter(reversed(range(len(result)+1, (i+1)+1))))
        return "".join(map(str, result))
