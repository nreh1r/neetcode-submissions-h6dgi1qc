class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.res = []

        def dfs(i, subset, val):
            if val == target:
                self.res.append(subset.copy())
                return
            
            if i >= len(nums) or val > target:
                return
            
            subset.append(nums[i])
            dfs(i, subset, val + nums[i])
            subset.pop()
            dfs(i + 1, subset, val)
        
        dfs(0, [], 0)

        return self.res