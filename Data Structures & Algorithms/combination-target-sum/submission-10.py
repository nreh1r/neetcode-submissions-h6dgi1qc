class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.res = []

        curr = []
        def dfs(i, curr, val):
            if val == target:
                self.res.append(curr.copy())
                return

            if i >= len(nums) or val > target:
                return
            
            curr.append(nums[i])
            dfs(i, curr, val + nums[i])
            curr.pop()
            dfs(i + 1, curr, val)
        
        dfs(0, [], 0)

        return self.res

            