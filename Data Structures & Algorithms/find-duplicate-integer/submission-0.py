class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        num_map = defaultdict(int)
        for num in nums:
            if num in num_map:
                return num
            num_map[num] += 1