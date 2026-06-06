class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        heap = [cnt for cnt in counts.values()]
        heapq.heapify_max(heap)

        queue = deque()
        count = 0
        while heap or queue:
            count += 1

            if heap:
                remaining = heapq.heappop_max(heap) - 1

                if remaining:
                    queue.append([remaining, count + n])
            
            if queue and queue[0][1] == count:
                heapq.heappush_max(heap, queue.popleft()[0])
        
        return count