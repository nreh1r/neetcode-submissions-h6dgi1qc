class Solution:
	def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
		self.res = []
		nums.sort()
		
		def dfs(i, subset):
			if i >= len(nums):
				self.res.append(subset.copy())
				return
			
			val = nums[i]
			subset.append(val)
			
			dfs(i + 1, subset)
			
			subset.pop()
			
			while i < len(nums) and nums[i] == val:
				i += 1
			
			dfs(i, subset)
		
		dfs(0, [])
		
		return self.res