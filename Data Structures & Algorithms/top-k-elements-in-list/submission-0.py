class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_counts = {}
        for num in nums:
            if num in num_counts:
                num_counts[num] += 1
            else:
                num_counts[num] = 1

        sorted_counts = sorted(list(num_counts.items()), reverse=True, key=lambda x: x[1])
        solution = []
        for i in range(k):
            solution.append(sorted_counts[i][0])
        return solution