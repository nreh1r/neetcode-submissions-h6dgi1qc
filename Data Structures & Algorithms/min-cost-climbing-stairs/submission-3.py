class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 2:
            return min(cost[0], cost[1])
        
        n1, n2 = cost[0], cost[1]

        for i in range(2, len(cost)):
            new = cost[i] + min(n1, n2)
            n1 = n2
            n2 = new
        return min(n1, n2)


        
