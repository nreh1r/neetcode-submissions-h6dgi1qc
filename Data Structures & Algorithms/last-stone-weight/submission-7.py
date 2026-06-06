class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = stones
        heapq.heapify_max(heap)

        while len(heap) > 1:
            x = heapq.heappop_max(heap)
            y = heapq.heappop_max(heap)

            if x - y > 0:
                heapq.heappush_max(heap, x - y)

        return heap[0] if len(heap) > 0 else 0