class DetectSquares:
    def __init__(self):
        self.point_frequency = Counter()
        self.x_coordinate = defaultdict(Counter)

    def add(self, point):
        x, y = point
        self.point_frequency[x, y] += 1
        self.x_coordinate[x][y] += 1

    def count(self, point):
        x, y = point
        ans = 0
        for y2 in self.x_coordinate[x]:
            if y == y2: continue
            ans += self.point_frequency[x, y2] * self.point_frequency[x + y2 - y, y] * self.point_frequency[x + y2 - y, y2]
            ans += self.point_frequency[x, y2] * self.point_frequency[x + y - y2, y] * self.point_frequency[x + y - y2, y2]
        return ans
