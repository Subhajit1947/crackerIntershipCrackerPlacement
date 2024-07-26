class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d=collections.defaultdict(list)
        for i in strs:
            a=''.join(sorted(i))
            d[a].append(i)

        return d.values()