class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for s in strs:
            coded_chars = [0] * 26
            for ch in s:
                coded_chars[ord(ch) - ord('a')] += 1
            ans[tuple(coded_chars)].append(s)
        return list(ans.values())