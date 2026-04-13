class Solution:
    def climbStairs(self, n: int) -> int:
        self.memoized = {
            0: 0,
            1: 1,
        }
        return self.fibonnaci(n + 1)
    
    def fibonnaci(self, n):
        if n in self.memoized:
            return self.memoized[n]
        
        val = self.fibonnaci(n - 2) + self.fibonnaci(n - 1)
        self.memoized[n] = val

        return val