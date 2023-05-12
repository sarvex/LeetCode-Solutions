# Time:  O(n)
# Space: O(1)

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        def length(it, start, c):
            depth, longest = 0, 0
            for i in it:
                if s[i] == c:
                    depth += 1
                else:
                    depth -= 1
                    if depth < 0:
                        start, depth = i, 0
                    elif depth == 0:
                        longest = max(longest, abs(i - start))
            return longest

        return max(length(xrange(len(s)), -1, '('), \
                   length(reversed(xrange(len(s))), len(s), ')'))


# Time:  O(n)
# Space: O(n)
class Solution2(object):
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        longest, last, indices = 0, -1, []
        for i in xrange(len(s)):
            if s[i] == '(':
                indices.append(i)
            elif not indices:
                last = i
            else:
                indices.pop()
                longest = max(longest, i - indices[-1]) if indices else max(longest, i - last)
        return longest

