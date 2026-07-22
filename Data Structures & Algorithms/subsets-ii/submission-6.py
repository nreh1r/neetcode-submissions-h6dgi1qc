class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        nums.sort()

        def dfs(i, subset):
            self.res.append(subset.copy())
            
            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j - 1]:
                    continue
                
                subset.append(nums[j])
                dfs(j + 1, subset)
                subset.pop()

        dfs(0, [])

        return self.res