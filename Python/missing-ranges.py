# Time:  O(n)
# Space: O(1)

class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        def getRange(lower, upper):
            return "{}".format(lower) if lower == upper else "{}->{}".format(lower, upper)

        ranges = []
        pre = lower - 1

        for i in xrange(len(nums) + 1):
            cur = upper + 1 if i == len(nums) else nums[i]
            if cur - pre >= 2:
                ranges.append(getRange(pre + 1, cur - 1))

            pre = cur

        return ranges


