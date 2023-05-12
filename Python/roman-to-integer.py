# Time:  O(n)
# Space: O(1)

class Solution(object):
    # @return an integer
    def romanToInt(self, s):
        numeral_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C":100, "D": 500, "M": 1000}
        return sum(
            numeral_map[s[i]] - 2 * numeral_map[s[i - 1]]
            if i > 0 and numeral_map[s[i]] > numeral_map[s[i - 1]]
            else numeral_map[s[i]]
            for i in xrange(len(s))
        )

