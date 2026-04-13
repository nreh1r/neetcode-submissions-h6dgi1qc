class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap, self.k = nums, k
        heapq.heapify(self.heap)
        # while len(self.heap) > k:
        #     heapq.heappop(self.heap)


    def add(self, val: int) -> int:
        # heapq.heappush(self.heap, val)
        # if len(self.heap) > self.k:
        #     heapq.heappop(self.heap)
        # return self.heap[0]
        heap_nodes = []
        heapq.heappush(self.heap, val)
        for _ in range(len(self.heap) - self.k):
            heap_nodes.append(heapq.heappop(self.heap))
        value = self.heap[0]
        for el in heap_nodes:
            heapq.heappush(self.heap, el)
        return value