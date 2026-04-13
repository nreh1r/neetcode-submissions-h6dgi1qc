class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # num_set = set(nums)
        # return len(num_set) != len(nums)
        # Alternative is use a map

        num_map = {}
        for num in nums:
            if num in num_map:
                return True
            else:
                num_map[num] = num
        return False