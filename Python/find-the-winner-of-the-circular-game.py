# Time:  O(n)
# Space: O(1)

# bottom-up solution
class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        return reduce(lambda idx, n:(idx+k)%(n+1), xrange(1, n), 0)+1


# Time:  O(n)
# Space: O(n)
# top-down solution
class Solution2(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        def f(idx, n, k):
            return 0 if n == 1 else (k+f((idx+k)%n, n-1, k))%n

        return f(0, n, k)+1
