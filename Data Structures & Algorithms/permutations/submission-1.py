class Solution:
	def permute(self, nums: List[int]) -> List[List[int]]:
		self.res = []
		
		def dfs(curr_set, left):
			if not left:
				self.res.append(curr_set.copy())
				return
			
			for i in range(len(left)):
				num = left[i]
				curr_set.append(num)
				
				updated = [val for val in left if val != num]
				
				dfs(curr_set, updated)
				
				curr_set.pop()
		
		dfs([], nums.copy())
		
		return self.res