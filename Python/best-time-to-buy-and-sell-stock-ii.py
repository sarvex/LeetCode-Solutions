# Time:  O(n)
# Space: O(1)


class Solution(object):
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        return sum(max(0, prices[i + 1] - prices[i]) for i in xrange(len(prices) - 1))

    def maxProfit2(self, prices):
        return sum(map(lambda x: max(prices[x + 1] - prices[x], 0),
                       xrange(len(prices[:-1]))))

