class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        smallest_number = float("inf")

        while l <= r:
            m = (l + r) // 2
            smallest_number = min(smallest_number, nums[m])
            if nums[m] > nums[-1]:
                l = m + 1
            elif nums[m] < nums[-1]:
                r = m - 1
            else:
                break
        
        return smallest_number