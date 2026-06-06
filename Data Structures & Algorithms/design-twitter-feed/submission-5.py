class Twitter:

	def __init__(self):
		self.tweets = []
		heapq.heapify_max(self.tweets)
		self.users = defaultdict(set)
		self.count = 0
	
	def postTweet(self, userId: int, tweetId: int) -> None:
		heapq.heappush_max(self.tweets, (self.count, tweetId, userId))
		self.count += 1
	
	def getNewsFeed(self, userId: int) -> List[int]:
		queue = deque()
		feed = []
		
		while self.tweets and len(feed) < 10:
			tweet = heapq.heappop_max(self.tweets)
			
			if tweet[2] == userId or tweet[2] in self.users[userId]:
				feed.append(tweet[1])
			
			queue.append(tweet)
		
		while queue:
			heapq.heappush_max(self.tweets, queue.popleft())
		
		return feed
	
	def follow(self, followerId: int, followeeId: int) -> None:
		self.users[followerId].add(followeeId)
	
	def unfollow(self, followerId: int, followeeId: int) -> None:
		self.users[followerId].discard(followeeId)
        
