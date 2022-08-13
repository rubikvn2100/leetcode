class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        len_word = len(word)
        visited = [[False] * m for row in range(n)]

        def helper(x: int, y: int, i: int) -> bool:
            if i == len_word:
                return True
            
            if not(0 <= x and x < n and 0 <= y and y < m):
                return False
            
            if visited[x][y]:
                return False
            
            if board[x][y] != word[i]:
                return False
            
            visited[x][y] = True
            if helper(x + 1, y, i + 1) or helper(x - 1, y, i + 1) or helper(x, y + 1, i + 1) or helper(x, y - 1, i + 1):
                return True
            visited[x][y] = False
            
            return False
            
        for i in range(n):
            for j in range(m):
                if helper(i, j, 0):
                    return True
                
        return False