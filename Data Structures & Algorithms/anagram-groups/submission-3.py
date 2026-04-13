class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        
        for s in strs:
            chars = [0] * 26
            for c in s:
                chars[ord(c) - ord('a')] += 1
            tup_i = tuple(chars)
            if tup_i in ans:
                ans[tup_i].append(s)
            else:
                ans[tup_i] = [s]
        return ans.values()