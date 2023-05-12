# Time:  O(logn), where logn is the length of result strings
# Space: O(1)

class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        dvd, dvs = abs(numerator), abs(denominator)
        result = (
            "-"
            if (numerator > 0 and denominator < 0)
            or (numerator < 0 and denominator > 0)
            else ""
        ) + str(dvd / dvs)
        dvd %= dvs

        if dvd > 0:
            result += "."

        lookup = {}
        while dvd and dvd not in lookup:
            lookup[dvd] = len(result)
            dvd *= 10
            result += str(dvd / dvs)
            dvd %= dvs

        if dvd in lookup:
            result = f"{result[:lookup[dvd]]}({result[lookup[dvd]:]})"

        return result


