class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        self.cost = cost
        self.cache = {}
        return min(self.recursive_search(len(cost) - 1), self.recursive_search(len(cost) - 2))
    
    def recursive_search(self, n):
        if n in self.cache:
            return self.cache[n]

        if n < 0:
            return 0

        val = self.cost[n] + min(self.recursive_search(n - 1), self.recursive_search(n - 2))
        self.cache[n] = val
        return val
        

        
