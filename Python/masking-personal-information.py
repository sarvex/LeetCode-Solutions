# Time:  O(1)
# Space: O(1)

class Solution(object):
    def maskPII(self, S):
        """
        :type S: str
        :rtype: str
        """
        if '@' in S:
            first, after = S.split('@')
            return f"{first[0]}*****{first[-1]}@{after}".lower()

        digits = filter(lambda x: x.isdigit(), S)
        local = f"***-***-{digits[-4:]}"
        return local if len(digits) == 10 else f"+{'*' * (len(digits) - 10)}-{local}"

