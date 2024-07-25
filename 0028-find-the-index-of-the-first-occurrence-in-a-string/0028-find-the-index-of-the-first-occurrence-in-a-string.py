class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        haystack=[i for i in haystack]
        needle=[i for i in needle]
        for i in range(len(haystack)):
            if haystack[i:i+len(needle)]==needle:
                return i
        return -1