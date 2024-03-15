'''
We can shift a string by shifting each of its letters to its successive letter.

For example, "abc" can be shifted to be "bcd".
We can keep shifting the string to form a sequence.

For example, we can keep shifting "abc" to form the sequence: "abc" -> "bcd" -> ... -> "xyz".
Given an array of strings strings, group all strings[i] that belong to the same shifting sequence. Y
'''
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:

        def hash(string: str):
            # normalize to start with "a"+
            shift = ord(string[0]) - ord('a')
            return ''.join([chr((ord(ch) - shift) % 26) for ch in string])  # need mod 26!

        groups = collections.defaultdict()
        for string in strings:
            hashed = hash(string)
            if hashed in groups:
                groups[hashed].append(string)
            else:
                groups[hashed] = [string]
        return list(groups.values())