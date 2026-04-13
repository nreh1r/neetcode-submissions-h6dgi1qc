class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)

        longest = 0
        i = 0
        while i < len(nums):
            # Check if the value is the start of the subsequence
            if nums[i] - 1 not in num_set:
                length = 1
                num = nums[i]
                while num + 1 in num_set:
                    length += 1
                    num += 1
                longest = max(longest, length)
            i += 1
        return longest 
            