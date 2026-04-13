class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []

        for i, a in enumerate(nums):
            if a > 0:
                break
            
            if i > 0 and nums[i - 1] == a:
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                sum_val = a + nums[l] + nums[r]

                if sum_val > 0:
                    r -= 1
                elif sum_val < 0:
                    l += 1
                else:
                    output.append([a, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l - 1] == nums[l]:
                        l += 1
            
        return output
