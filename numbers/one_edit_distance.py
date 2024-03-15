'''
Given two strings s and t, return true if they are both one edit distance apart, otherwise return false.

A string s is said to be one distance apart from a string t if you can:

Insert exactly one character into s to get t.
Delete exactly one character from s to get t.
Replace exactly one character of s with a different character to get t.

'''
    def isOneEditDistance(self, s: str, t: str) -> bool:
        ns, nt = len(s), len(t)
        # ensure the order (similar to how we first order the list before merging intervals)
        if ns > nt:
            return self.isOneEditDistance(t, s)
        # basic case
        if nt - ns > 1:
            return False
        # loop the short string, if char diff, check replace or add
        for i in range(ns):
            if s[i] != t[i]:
                # replace case
                if ns == nt:
                    return s[i+1:] == t[i+1:]
                # add case
                return s[i:] == t[i+1:]
        return ns+1 == nt    # handle when the short string is empty