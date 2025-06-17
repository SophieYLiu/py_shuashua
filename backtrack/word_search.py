"""
Word search I.
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Time: O(m*n)
"""
class Solution_WordSearch_I:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def dfs(i, j, idx):
            if board[i][j] == word[idx] and idx == len(word) - 1:
                return True
            if idx >= len(word):
                return False
            if board[i][j] != word[idx]:
                return False
            for a, b in dirs:
                x, y = a + i, b + j
                if 0 <= x < m and 0 <= y < n:
                    temp = board[i][j]
                    board[i][j] = '#'
                    if dfs(x, y, idx + 1):
                        return True
                    board[i][j] = temp
            return False

        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
        return False


''' 
Notes:
1. for traverse a word in trie: 最开始状态 - root children 对应 1st letter in the word
2. don't return when find one match, need continue search
3. trie node structure：is_end和content是对应的，when is_end is True, the content is the full word. This can be useful
4. pass the TrieNode in recusive fun to save time!
'''


class TrieNode:
    def __init__(self, content=""):
        self.content = content  # sentence
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
        cur.is_end = True
        cur.content = word


class Solution_WordSearch_II:

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board:
            return []
        res = []
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        m, n = len(board), len(board[0])

        def dfs(i, j, node):
            ch = board[i][j]
            # prunning
            if ch not in node.children:
                return
            cur = node.children[ch]
            if cur.is_end:
                res.append(cur.content)

            t = board[i][j]
            board[i][j] = '#'
            for x, y in dirs:
                nexti, nextj = i + x, j + y
                if 0 <= nexti < m and 0 <= nextj < n and board[nexti][nextj] != '#':
                    dfs(nexti, nextj, cur)
            board[i][j] = t
            return

        # build trie
        voc_tree = Trie()
        for word in words:
            voc_tree.insert(word)

        # loop
        for i in range(m):
            for j in range(n):
                dfs(i, j, voc_tree.root)
        return list(set(res))
