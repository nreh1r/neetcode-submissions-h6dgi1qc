class TimeMap:
	def __init__(self):
		self.cache = defaultdict(list)

	def set(self, key: str, value: str, timestamp: int) -> None:
		self.cache[key].append((value, timestamp))

	def get(self, key: str, timestamp: int) -> str:
		values = self.cache[key]
		
		time_to_search = timestamp
		while time_to_search > 0:
			l, r = 0, len(values) - 1
			
			while l <= r:
				m = (l + r) // 2
				
				if values[m][1] > time_to_search:
					r = m -1
				elif values[m][1] < time_to_search:
					l = m + 1
				else:
					return values[m][0]
			
			time_to_search -= 1
		
		return ""