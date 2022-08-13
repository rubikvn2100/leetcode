class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # A node will contain:
        # 1/ dictionary of pointer to children
        # 2/ pointer to parent
        # 3/ word if we sit in the end of the path that start from root that make up the word.
        # 4/ the character that store in the current node.
        root = [{}, None, None, None]
        for word in words:
            p = root
            for char in word[:-1]:
                if char not in p[0]:
                    p[0][char] = [{}, p, None, char]
                p = p[0][char]
            
            lastChar = word[-1]
            if lastChar not in p[0]:
                p[0][lastChar] = [{}, p, None, lastChar]
            p[0][lastChar][2] = word
            
        n = len(board)
        m = len(board[0])
        visited = [[False] * m for _ in range(n)]
        words_found = []
        def helper(x: int, y:int, p):
            children, parent, word, char = p
            if word is not None:
                words_found.append(word)
                p[2] = None
            
            if not(0 <= x and x < n and 0 <= y and y < m):
                return
            
            if visited[x][y]: 
                return
            
            current_char = board[x][y]
            if board[x][y] not in children:
                return
            
            visited[x][y] = True
            helper(x + 1, y    , children[current_char])
            helper(x - 1, y    , children[current_char])
            helper(x    , y + 1, children[current_char])
            helper(x    , y - 1, children[current_char])
            visited[x][y] = False
            
            if not word and not children:
                parent[0].pop(char)
                
        for x in range(n):
            for y in range(m):
                helper(x, y, root)
                
        return words_found