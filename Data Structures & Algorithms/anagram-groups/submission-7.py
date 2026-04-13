class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for s in strs:
            coded_list = [0] * 26
            for char in s:
                coded_list[ord('a') - ord(char)] += 1
            ans[tuple(coded_list)].append(s)
        
        return list(ans.values())