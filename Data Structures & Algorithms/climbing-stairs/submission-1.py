class Solution:
    def climbStairs(self, n: int) -> int:
        return self.fibonnaci(n + 1)
    
    def fibonnaci(self, n):
        if n == 0:
            return 0

        if n == 1:
            return 1
        
        return self.fibonnaci(n - 2) + self.fibonnaci(n - 1)