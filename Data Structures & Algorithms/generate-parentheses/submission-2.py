class Solution:
	def generateParenthesis(self, n: int) -> List[str]:
		self.res = []
		
		def dfs(open_used, closed_used, substring):
			if open_used == n and closed_used == n:
				self.res.append(substring)
				return
			
			if open_used < n:
				dfs(open_used + 1, closed_used, f"{substring}(")
			
			if closed_used < open_used:
				dfs(open_used, closed_used + 1, f"{substring})")
			
		
		dfs(0, 0, "")
		
		return self.res