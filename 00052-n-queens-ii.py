class Solution:
    def totalNQueens(self, n: int) -> int:
        result_count = [0]
        
        def DFS(k: int, board: list[list[int]]):
            if k == n:
                result_count[0] += 1
                return
                
            for col_idx in range(n):
                if board[k][col_idx]:
                    new_board = [[board[i][j] for j in range(n)] for i in range(n)]
                    for i in range(n):
                        new_board[i][col_idx] = False
                        
                        new_col_index = col_idx - (k - i)
                        if 0 <= new_col_index and new_col_index < n:
                            new_board[i][new_col_index] = False
                        
                        new_col_index = col_idx + (k - i)
                        if 0 <= new_col_index and new_col_index < n:
                            new_board[i][new_col_index] = False
                            
                    DFS(k + 1, new_board)
                
        DFS(0, [[True] * n for _ in range(n)])
        return result_count[0]
            