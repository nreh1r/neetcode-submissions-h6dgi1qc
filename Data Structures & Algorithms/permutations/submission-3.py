class Solution:
	def permute(self, nums: List[int]) -> List[List[int]]:
		self.res = []
		
		def dfs(first):
			if first == len(nums):
				self.res.append(nums.copy())
				return
			
			for i in range(first, len(nums)):
				nums[first], nums[i] = nums[i], nums[first]
				
				dfs(first + 1)
				
				nums[first], nums[i] = nums[i], nums[first]
		
		dfs(0)
		
		return self.res