from typing import List


class Trie:

    def __init__(self):
        self.trie = {}

    def insert(self, word):
        cur = self.trie
        for ch in word:
            if ch not in cur:
                cur[ch] = {}
            cur = cur[ch]
        cur['end'] = True

    def search_prefix(word):
        cur = self.trie
        for ch in word:
            if ch in cur:
                cur = cur[ch]
            else:
                return False
        return True

class Solution:

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board:
            return []
        res = []
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        m, n = len(board), len(board[0])

        # O(n)
        def find_prefix(w, words):
            for word in words:
                if word.startswith(w):
                    return True
            return False

        def dfs(i, j, temp):
            # if temp in res: # cant do this - even if you found one, you still need keep looking for more, dont return
            #     return
            if temp in words:
                res.append(str(temp))
            if not (0 <= i < m and 0 <= j < n):
                return
            if board[i][j] == '#':
                return
            # if not find_prefix(temp, words):
            #     return
            if not voc_tree.search_prefix(temp):
                return
            t = board[i][j]
            board[i][j] = '#'
            for x, y in dirs:
                nexti, nextj = i + x, j + y
                # print("going in:", temp+t)
                dfs(nexti, nextj, temp + t)
            board[i][j] = t
            return

        voc_tree = Trie()
        for word in words:
            voc_tree.insert(word)

        for i in range(m):
            for j in range(n):
                # print("*****", i, j)
                dfs(i, j, "")
        return list(set(res))
