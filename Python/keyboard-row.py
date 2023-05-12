# Time:  O(n)
# Space: O(1)

class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        rows = [
            {'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'},
            {'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'},
            {'z', 'x', 'c', 'v', 'b', 'n', 'm'},
        ]

        result = []
        for word in words:
            k = next((i for i in xrange(len(rows)) if word[0].lower() in rows[i]), 0)
            for c in word:
                if c.lower() not in rows[k]:
                    break
            else:
                result.append(word)
        return result


class Solution2(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        keyboard_rows = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
        single_row_words = []
        for word in words:
            single_row_words.extend(
                word
                for row in keyboard_rows
                if all(letter in row for letter in word.lower())
            )
        return single_row_words

