class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        result = ""

        for i in range(len(strs[0])):
            char = strs[0][i]

            for word in strs[1:]:
                if i >= len(word) or word[i] != char:
                    return result

            result += char

        return result
        """
        :type strs: List[str]
        :rtype: str
        """
        