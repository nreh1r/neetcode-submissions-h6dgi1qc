class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in nums:
            if num - 1 in num_set:
                continue

            current_sequence = 1
            while num + 1 in num_set:
                current_sequence += 1
                num += 1
            
            longest = max(longest, current_sequence)
        return longest
            