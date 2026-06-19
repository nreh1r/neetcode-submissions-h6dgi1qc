class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        res_map = {}

        subset = []
        def dfs(i, calc):
            if calc[1] > target:
                return
            elif calc[1] == target:
                solution = subset.copy()
                if tuple(solution) not in res_map:
                    res.append(solution)
                    res_map[tuple(solution)] = True
                return
            elif i >= len(nums):
                return
            new_arr = calc[0]
            new_arr.append(nums[i])
            dfs(i, [new_arr, calc[1] + nums[i]])
            dfs(i + 1, [new_arr, calc[1] + nums[i]])
            new_arr.pop()
            dfs(i + 1, [new_arr, calc[1]])
        
        dfs(0, [subset, 0])

        return res