# Time:  O(n)
# Space: O(1)

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        result = []
        i, j, carry = len(num1) - 1, len(num2) - 1, 0

        while i >= 0 or j >= 0 or carry:
            if i >= 0:
                carry += ord(num1[i]) - ord('0')
                i -= 1
            if j >= 0:
                carry += ord(num2[j]) - ord('0')
                j -= 1
            result.append(str(carry % 10))
            carry /= 10
        result.reverse()

        return "".join(result)

    def addStrings2(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        length = max(len(num1), len(num2))
        num1 = num1.zfill(length)[::-1]
        num2 = num2.zfill(length)[::-1]
        res, plus = '', 0
        for index, num in enumerate(num1):
            tmp = str(int(num) + int(num2[index]) + plus)
            res += tmp[-1]
            plus = 1 if int(tmp) > 9 else 0
        if plus:
            res += '1'
        return res[::-1]

