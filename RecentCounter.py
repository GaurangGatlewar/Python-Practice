class RecentCounter:

    def __init__(self):
        self.timeStamp = []

    def ping(self, t: int) -> int:
        self.timeStamp.append(t)
        while len(self.timeStamp)>0:
            if self.timeStamp[0]<t-3000:
                self.timeStamp.pop(0)
            else:
                break
        return len(self.timeStamp)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)