# Time:  O(n)
# Space: O(1)

class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = max(nums)
        return nums.index(m) if all(m >= 2*x for x in nums if x != m) else -1

