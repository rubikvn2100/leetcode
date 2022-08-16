class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result_lists = []
        def DFS(k: int, board: List[List[int]]):
            if k == n: 
                result_lists.append(["".join(["Q" if board[i][j] == 2 else "." for j in range(n)]) for i in range(n)])
                
                return
                
            for col_idx in range(n):
                if board[k][col_idx] == 0:
                    new_board = [[board[i][j] for j in range(n)] for i in range(n)]
                    for i in range(n):
                        if board[i][col_idx] == 0:
                            new_board[i][col_idx] = 1
                                     
                        new_col_idx = col_idx - (k - i)
                        if 0 <= new_col_idx and new_col_idx < n and board[i][new_col_idx] == 0:
                            new_board[i][new_col_idx] = 1
                                     
                        new_col_idx = col_idx + (k - i)
                        if 0 <= new_col_idx and new_col_idx < n and board[i][new_col_idx] == 0:
                            new_board[i][new_col_idx] = 1
                                   
                    new_board[k][col_idx] = 2
                
                    DFS(k + 1, new_board)
                    
        DFS(0, [[0] * n for _ in range(n)])
        
        return result_lists
                    
        