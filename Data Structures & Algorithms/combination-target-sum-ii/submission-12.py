class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []
        candidates.sort()

        def dfs(i, subset, val):
            if val == target:
                self.res.append(subset.copy())
                return
            
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                if val + candidates[j] > target:
                    break
                
                subset.append(candidates[j])
                dfs(j + 1, subset, val + candidates[j])
                subset.pop()
            
        dfs(0, [], 0)

        return self.res