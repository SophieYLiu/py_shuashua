class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        def is_subseq(tgt):
            """ test if tgt is sebseq of source """
            if len(source) < len(tgt):
                return False
            p = q = 0
            while p < len(source) and q < len(tgt):
                if source[p] == tgt[q]:
                    q += 1
                p += 1
            return q == len(tgt)

        @lru_cache
        def fun(source, tgt):
            if is_subseq(tgt):
                return 1
            ans = len(tgt)
            found = False
            for j in range(1, len(tgt)):
                former, latter = tgt[:j], tgt[j:]
                if is_subseq(former):
                    found = True
                    t = fun(source, latter)
                    if t == math.inf:
                        return math.inf
                    temp = t + 1
                    if temp < ans:
                        ans = temp
            return ans if found else math.inf

        res = fun(source, target)
        return res if res != math.inf else -1


# Better time complexity
class Solution:
    def shortestWay(self, source: str, target: str) -> int:

        def is_subseq(to_check, in_string):
            """ test if tgt is sebseq of source """
            if len(in_string) < len(to_check):
                return False
            p = q = 0
            while p < len(in_string) and q < len(to_check):
                if in_string[p] == to_check[q]:
                    q += 1
                p += 1
            return q == len(to_check)

        source_chars = set(source)
        if any(char not in source_chars for char in target):
            return -1

        concat_src = source
        count = 1
        while not is_subseq(target, concat_src):
            concat_src += source
            count += 1
        return count