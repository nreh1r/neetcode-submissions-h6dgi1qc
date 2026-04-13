class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for s in strs:
            count_arr = [0] * 26
            for char in s:
                count_arr[ord(char) - ord('a')] += 1
            ans[tuple(count_arr)].append(s)
        return list(ans.values())