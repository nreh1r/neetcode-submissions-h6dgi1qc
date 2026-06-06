class Twitter:

    def __init__(self):
        self.tweets = []
        heapq.heapify_max(self.tweets)
        self.users = defaultdict(set)
        self.post_count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        heapq.heappush_max(self.tweets, (self.post_count, tweetId, userId))
        self.post_count += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        queue = deque()
        feed = []

        while self.tweets and len(feed) < 10:
            tweet = heapq.heappop_max(self.tweets)
            if tweet[2] == userId or tweet[2] in self.users[userId]:
                feed.append(tweet[1])
            
            queue.append(tweet)
        
        while queue:
            tweet_to_add = queue.popleft()
            heapq.heappush_max(self.tweets, tweet_to_add)
        
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].discard(followeeId)
