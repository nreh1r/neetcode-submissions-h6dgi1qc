class Solution:
	def minEatingSpeed(self, piles: List[int], h: int) -> int:
		l, r = 1, max(piles)
		res = r
		
		while l <= r:
			speed = (l + r) // 2
			
			timeRequired = 0
			for pile in piles:
				timeRequired += math.ceil(float(pile) / speed)
			
			if timeRequired <= h:
				res = speed
				r = speed - 1
			else:
				l = speed + 1
		
		return res