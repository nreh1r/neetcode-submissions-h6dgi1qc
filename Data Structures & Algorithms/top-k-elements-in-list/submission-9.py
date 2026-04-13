class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = [[] for i in range(len(nums) + 1)]
        num_map = defaultdict(int)

        for num in nums:
            num_map[num] += 1
        
        for num, count in num_map.items():
            ans[count].append(num)
        
        counts = []
        for j in range(len(ans) - 1, -1, -1):
            curr_counts = ans[j]
            for l in range(len(curr_counts)):
                if len(counts) < k:
                    counts.append(curr_counts[l])
        
        return counts



