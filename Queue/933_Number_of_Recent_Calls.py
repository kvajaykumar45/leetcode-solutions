

class RecentCounter:

    def __init__(self):
        self.req = []

    def ping(self, t: int) -> int:
        self.req.append(t)
        count = 0
        ran = [(t - 3000) , t]
        for r in self.req:
            if(r >= ran[0] and r <= ran[1]):
                count += 1
        return count


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
