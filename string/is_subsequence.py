class Solution:
    # Time O(T), Space O(1)

    def isSubsequence_best(self, s: str, t: str) -> bool:
        i = j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)

    def isSubsequence_1(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        while i < len(s):
            while j < len(t):
                if i == len(s):
                    return True
                if s[i] == t[j]:
                    i += 1
                j += 1
            if j >= len(t) and i < len(s):
                return False
        return True

    # ALT: Slight better in writing
    def isSubsequence_2(self, s: str, t: str) -> bool:
        LEFT_BOUND, RIGHT_BOUND = len(s), len(t)

        p_left = p_right = 0
        while p_left < LEFT_BOUND and p_right < RIGHT_BOUND:
            # move both pointers or just the right pointer
            if s[p_left] == t[p_right]:
                p_left += 1
            p_right += 1

        return p_left == LEFT_BOUND

    # ALT: Just testing whether all characters in s are also in t (in order). Takes O(|s| + |t|) time and O(1) space.
    '''
First, we turned t into a iterator, and what that does is that "c in it" iterates through the iterator until the first position where it finds a match. 
Second, (c in it for c in s) is a generator: it returns an iterator.
Third, all() has only 1 parenthesis, so syntactic sugar: no need for double parentheses
all() takes in an iterator as an argument and loops through to find the first False. If it can't find it, it return True. 
    '''

    def isSubsequence2(self, s, t):
        t = iter(t)
        return all(c in t for c in s)

    # ALT
    def isSubsequence3(self, s, t):
        remainder_of_t = iter(t)
        for letter in s:
            if letter not in remainder_of_t:
                return False
        return True

    # ALT
    def isSubsequence4(self, s, t):
        for c in s:
            i = t.find(c)
            if i == -1:
                return False
            else:
                t = t[i + 1:]
        return True
