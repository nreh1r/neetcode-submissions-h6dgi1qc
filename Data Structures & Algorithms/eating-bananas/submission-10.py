class Solution:
	def minEatingSpeed(self, piles: List[int], h: int) -> int:
		l, r = 1, max(piles)
		res = 0

		while l <= r:
			m = (l + r) // 2

			totalTime = 0
			for pile in piles:
				totalTime += math.ceil(float(pile) / m)
			
			if totalTime <= h:
				res = m
				r = m - 1
			else:
				l = m + 1
		
		return res