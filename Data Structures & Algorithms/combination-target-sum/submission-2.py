class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(idx, subset, count):
            if count == target:
                res.append(subset.copy())
                return
            elif idx >= len(nums) or count > target:
                return
            
            subset.append(nums[idx])
            dfs(idx, subset, count + nums[idx])
            subset.pop()
            dfs(idx + 1, subset, count)
        
        dfs(0, [], 0)

        return res