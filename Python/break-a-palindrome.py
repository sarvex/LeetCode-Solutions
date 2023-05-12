# Time:  O(n)
# Space: O(1)

class Solution(object):
    def breakPalindrome(self, palindrome):
        """
        :type palindrome: str
        :rtype: str
        """
        return next(
            (
                f'{palindrome[:i]}a{palindrome[i + 1:]}'
                for i in xrange(len(palindrome) // 2)
                if palindrome[i] != 'a'
            ),
            f'{palindrome[:-1]}b' if len(palindrome) >= 2 else "",
        )
