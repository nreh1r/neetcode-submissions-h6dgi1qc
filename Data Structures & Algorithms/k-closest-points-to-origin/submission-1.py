class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        nums = []
        for point in points:
            nums.append((math.sqrt((point[0]**2 + point[1]**2)), point))
        
        heapq.heapify(nums)
        print(nums)


        res = []
        while len(res) < k:
            res.append(heapq.heappop(nums)[1])

        return res
