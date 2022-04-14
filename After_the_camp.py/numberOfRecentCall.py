class RecentCounter:

    def __init__(self,queue = []):
        self.queue = deque()

    def ping(self, t: int) -> int:
        x = t - 3000
        y = t
        self.queue.append(t)
        while self.queue[0] < x:
            self.queue.popleft()
        
        return len(self.queue)  

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
# time and space complexity
# time = O(n)
# space = 0(3001)