class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = [[] for i in range(len(nums) + 1)]
        num_map = defaultdict(int)

        for num in nums:
            num_map[num] += 1

        for num, count in num_map.items():
            counts[count].append(num)
        
        i = len(counts) - 1
        output = []
        while len(output) < k:
            for curr_count in counts[i]:
                if len(output) < k:
                    output.append(curr_count)
            i -= 1
        return output




