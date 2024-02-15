class Solution:
    def compress(self, chars: List[str]) -> int:

        # iterate the string to group the sequential same chars
        counts = []
        idx = 0
        while idx < len(chars):
            ch, cnt = chars[idx], 0
            while idx < len(chars) and ch == chars[idx]:
                cnt += 1
                idx += 1
            counts.append([ch, cnt])

        i = 0
        for ch, cnt in counts:
            print(ch, cnt)
            # add the character
            chars[i] = ch
            if cnt == 1:
                i += 1
                continue

            # add count
            cnt_str = str(cnt)
            for c in cnt_str:
                i += 1
                chars[i] = c

            i += 1
        return i
