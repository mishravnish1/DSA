class Solution(object):
    def longestCommonPrefix(self, strs):
        prefix = strs[0]

        for s in strs:
            while not s.startswith(prefix):
                prefix = prefix[:-1]

        return prefix
        """
        :type strs: List[str]
        :rtype: str
        """
        