# Time:  O(n)
# Space: O(1)

class Solution(object):
    def alphabetBoardPath(self, target):
        """
        :type target: str
        :rtype: str
        """
        x, y = 0, 0
        result = []
        for c in target:
            y1, x1 = divmod(ord(c)-ord('a'), 5)
            result.extend(
                (
                    'U' * max(y - y1, 0),
                    'L' * max(x - x1, 0),
                    'R' * max(x1 - x, 0),
                    'D' * max(y1 - y, 0),
                    '!',
                )
            )
            x, y = x1, y1
        return "".join(result)
