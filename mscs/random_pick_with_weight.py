class Solution:

    def __init__(self, w: List[int]):
        self.ps = []  # prefix sum has the same len of the input list w
        for weight in w:
            prev = 0 if not self.ps else self.ps[-1]
            self.ps.append(prev + weight)
        self.total = self.ps[-1]

    def pickIndex(self) -> int:
        import random
        import bisect
        target = random.random() * self.total  # a random number within the range 0-total

        # the rest is about search that random number idx from prefix sum list
        # return bisect.bisect_left(self.ps, target)
        low, high = 0, len(self.ps) - 1
        while low < high:
            mid = low + (high - low) // 2
            if target > self.ps[mid]:
                low = mid + 1
            else:
                high = mid
        return low

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()