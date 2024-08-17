class RecentCounter:

    def __init__(self):
        self.queue = []
    def ping(self, t: int) -> int:
        self.queue.append(t)
        counter = 0
        while self.queue[0] < t - 3000:
            self.queue.pop(0)
        return len(self.queue)

# The fact that this question is there is on leetcode is sad!

