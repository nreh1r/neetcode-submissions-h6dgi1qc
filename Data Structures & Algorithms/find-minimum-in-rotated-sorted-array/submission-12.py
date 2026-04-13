class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        min_value = nums[0]

        while l <= r:
            if nums[l] < nums[r]:
                min_value = min(min_value, nums[l])
                break

            m = (l + r) // 2
            min_value = min(min_value, nums[m])
            if nums[l] <= nums[m]:
                l = m + 1
            else:
                r = m - 1

        return min_value

        
            