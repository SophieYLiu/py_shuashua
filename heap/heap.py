class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import collections
        # counts = dict(collections.Counter(nums))
        # ordered_counts = sorted(counts.items(), key=lambda x: -x[1])
        # res = [each[0] for each in ordered_counts[:k]]
        # return res
        table = collections.defaultdict(int)
        for num in nums:
            table[num] += 1
        import heapq
        pq = []
        for num, cnt in table.items():
            if not pq or len(pq) < k:
                heapq.heappush(pq, [cnt, num])
                continue

            if len(pq) == k and pq[0][0] < cnt:
                heapq.heappop(pq)
                heapq.heappush(pq, [cnt, num])
        return [item[1] for item in pq]


class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        jobs = zip(difficulty, profit)
        jobs.sort()
        ans = i = best = 0
        for skill in sorted(worker):
            while i < len(jobs) and skill >= jobs[i][0]:
                best = max(best, jobs[i][1])
                i += 1
            ans += best
        return ans
