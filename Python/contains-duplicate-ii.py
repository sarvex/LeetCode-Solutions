# Time:  O(n)
# Space: O(n)

class Solution(object):
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        lookup = {}
        for i, num in enumerate(nums):
            if num in lookup and i - lookup[num] <= k:
                return True
            lookup[num] = i
        return False

