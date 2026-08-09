class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()
    
    def add_word(self, word):
        curr = self.root

        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.word = word
    
    def get_root(self):
        return self.root

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows, cols = len(board), len(board[0])
        self.res, path = set(), set()
        tree = PrefixTree()

        for word in words:
            tree.add_word(word)
        
        def dfs(row, col, node):
            if node.word:
                self.res.add(node.word)
            
            if (
                row < 0 or col < 0 or
                row >= rows or col >= cols or
                board[row][col] not in node.children or
                (row, col) in path
            ):
                return
            
            path.add((row, col))

            dfs(row + 1, col, node.children[board[row][col]])
            dfs(row - 1, col, node.children[board[row][col]])
            dfs(row, col + 1, node.children[board[row][col]])
            dfs(row, col - 1, node.children[board[row][col]])

            path.remove((row, col))
        
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, tree.get_root())
        
        return list(self.res)