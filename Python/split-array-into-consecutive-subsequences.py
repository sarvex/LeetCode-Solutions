# Time:  O(n)
# Space: O(1)

class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        pre, cur = float("-inf"), 0
        cnt1, cnt2, cnt3 = 0, 0, 0
        i = 0
        while i < len(nums):
            cnt = 0
            cur = nums[i]
            while i < len(nums) and cur == cur:
                cnt += 1
                i += 1

            if (
                cur == pre + 1
                and cnt < cnt1 + cnt2
                or cur != pre + 1
                and (cnt1 != 0 or cnt2 != 0)
            ):
                return False
            elif cur == pre + 1:
                cnt1, cnt2, cnt3 = max(0, cnt - (cnt1 + cnt2 + cnt3)), \
                                       cnt1, \
                                       cnt2 + min(cnt3, cnt - (cnt1 + cnt2))
            else:
                cnt1, cnt2, cnt3 = cnt, 0, 0
            pre = cur
        return cnt1 == 0 and cnt2 == 0

