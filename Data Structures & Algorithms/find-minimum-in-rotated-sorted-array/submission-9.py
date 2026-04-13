class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        min_val = nums[0]

        while l <= r:
            if nums[l] < nums[r]:
                min_val = min(min_val, nums[l])
                break
            
            m = (l + r) // 2
            min_val = min(min_val, nums[m])

            if nums[l] <= nums[m]:
                l = m + 1
            else:
                r = m - 1
        
        return min_val
            