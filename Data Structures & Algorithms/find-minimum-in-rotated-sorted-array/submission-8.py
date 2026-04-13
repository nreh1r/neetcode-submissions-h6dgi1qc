class Solution:
	def findMin(self, nums: List[int]) -> int:
		l, r = 0, len(nums) - 1
		min_value = nums[0]
		
		while l <= r:
			# Check if the current sub list is already sorted
			# If so we can stop because we have are in a sorted portion
			# So we can update min_value and stop looping
			if nums[l] < nums[r]:
				min_value = min(min_value, nums[l])
				break
				
			m = (l + r) // 2
			min_value = min(min_value, nums[m])
			
			# Need to determine how to move through the list
			# We check the current value with the value on the leftmost part
			# Of the sublist. Because we know the right side of the sub list
			# Is smaller than the left, if the value at nums[m] is
			# >= nums[l] then we are in the part of the list that was
			# Rotated, so we want to move to the right for searching
			if nums[m] >= nums[l]:
				l = m + 1
			else:
				# Here we have already entered the sorted sub list that
				# contains the smaller numbers so we go left to try to find
				# The smallest value
				r = m - 1
			
		return min_value