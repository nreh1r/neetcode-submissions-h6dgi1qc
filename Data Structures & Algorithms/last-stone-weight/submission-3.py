class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Make stone weights negative for max heap
        max_heap = [-1 * el for el in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            x = heapq.heappop(max_heap)
            y = heapq.heappop(max_heap)

            if y > x:
                heapq.heappush(max_heap, x - y)
            
        return -1 * max_heap[0] if max_heap else 0