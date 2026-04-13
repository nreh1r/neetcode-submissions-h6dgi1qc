class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_counts = {}
        frequency = [[] for i in range(len(nums) + 1)]

        for num in nums:
            num_counts[num] = 1 + num_counts.get(num, 0)
        for n, c in num_counts.items():
            frequency[c].append(n)

        res = []
        for i in range(len(frequency) - 1, 0, -1):
            for n in frequency[i]:
                res.append(n)
                if len(res) == k:
                    return res
