class MedianFinder:

    def __init__(self):
        self.heap = []
        heapq.heapify(self.heap)

    def addNum(self, num: int) -> None:
        heapq.heappush(self.heap, float(num))

    def findMedian(self) -> float:
        queue = deque()
        if len(self.heap) == 1:
            return self.heap[0]

        is_even = True if len(self.heap) % 2 == 0 else False
        print(self.heap)
        first_index, second_index = None, None
        mid = len(self.heap) / 2

        if is_even:
            first_index = math.floor(mid - 1)
            second_index = first_index + 1
        else:
            first_index = math.floor(mid)

        first_num, second_num = None, None
        i = 0
        print("index", first_index, second_index)
        while self.heap:
            value = heapq.heappop(self.heap)
            if i == first_index:
                first_num = value
            elif i == second_index and is_even:
                second_num = value
            
            queue.append(value)
            i += 1
        print(first_num, second_num)

        while queue:
            heapq.heappush(self.heap, queue.popleft())

        if second_num:
            return (first_num + second_num) / 2
        
        return first_num


        