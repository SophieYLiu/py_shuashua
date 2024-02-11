class Solution:
    ''' for each item in the list, compare it with the new interval (which is updated throughout, and decide to add itself, or updated new interval or wait for next iteration)'''
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        def intersect(a, b):
            return a[0] <= b[0] <= a[1] or b[0] <= a[0] <= b[1]
        res = []

        # SOL1. Use Sort
        # for itv in intervals:
        #     if not intersect(itv, newInterval):
        #         res.append(itv)
        #     else:
        #         newInterval = [min(itv[0], newInterval[0]), max(itv[1], newInterval[1])]
        # res.append(newInterval)
        # return sorted(res, key=lambda itm: itm[0])
        
        # SOL2. No Sort
        for itv in intervals:
            if itv[0] > newInterval[1]:
                res.append(newInterval)
                newInterval = itv
            elif itv[1] < newInterval[0]:
                res.append(itv)
            elif intersect(itv, newInterval):
                newInterval = [min(itv[0], newInterval[0]), max(itv[1], newInterval[1])]
        res.append(newInterval)
        return res

                