class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        largest_sequence = 0
        for num in nums:
            if num - 1 in num_set:
                continue

            sequence = 0

            while num in num_set:
                num += 1
                sequence += 1

            largest_sequence = max(largest_sequence, sequence)
        
        return largest_sequence
            