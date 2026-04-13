class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, a in enumerate(nums):
            if a > 0:
                break
            
            if i > 0 and nums[i - 1] == a:
                continue
            
            l, r = i + 1, len(nums) - 1

            while l < r:
                val = a + nums[l] + nums[r]

                if val < 0:
                    l += 1
                elif val > 0:
                    r -= 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res

