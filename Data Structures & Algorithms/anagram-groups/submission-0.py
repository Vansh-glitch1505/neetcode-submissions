class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for c in strs:
            sortedC = ''.join(sorted(c))
            res[sortedC].append(c)

        return list(res.values())