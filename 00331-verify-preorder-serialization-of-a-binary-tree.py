class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        token_arr = preorder.split(',')
        n = len(token_arr)
        
        stack = []
        for i, token in enumerate(token_arr):
            if token == '#':
                while True:
                    if not stack:
                        return True if i == n - 1 else False
                    
                    val, side = stack.pop()
                    if side == "L":
                        stack.append([val, "R"])
                        break
            else:
                stack.append([token, "L"])
                
        return True if not stack else False
    