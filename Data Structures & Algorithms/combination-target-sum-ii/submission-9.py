class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []
        self.cache = {}
        candidates.sort()

        def dfs(i, subset, val):
            if val == target:
                self.res.append(subset.copy())
                return

            if i >= len(candidates) or val > target:
                return
            
            subset.append(candidates[i])
            dfs(i + 1, subset, val + candidates[i])
            subset.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1

            dfs(i + 1, subset, val)
        
        dfs(0, [], 0)

        return self.res