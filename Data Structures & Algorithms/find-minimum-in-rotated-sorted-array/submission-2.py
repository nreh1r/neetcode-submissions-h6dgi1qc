class Solution:
	def findMin(self, nums: List[int]) -> int:
		l, r = 0, len(nums) - 1
		smallest_number = float("inf")
		
		while l <= r:
			m = (l + r) // 2
			smallest_number = min(smallest_number, nums[m])
			
			if nums[m] > nums[-1]:
				# If the current element is bigger than the end element
				# We know the smallest number is to the right
				l = m + 1
			elif nums[m] < nums[-1]:
				# If the current element is smaller than the end element
				# We know the smallest number is to the left
				r = m - 1
			else:
				# All the numbers are unique so if the equal condition fires
				# We can just break out because we are done the search
				break
		
		return smallest_number