class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = [[] for i in range(len(nums) + 1)]
        num_map = defaultdict(int)

        for num in nums:
            num_map[num] += 1
        
        for key, val in num_map.items():
            ans[val].append(key)
        
        output = []
        i = len(ans) - 1
        while len(output) < k:
            for num in ans[i]:
                if len(output) < k:
                    output.append(num)
            i -= 1
        
        return output


