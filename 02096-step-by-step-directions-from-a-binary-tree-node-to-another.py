# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def helper(root: Optional[TreeNode], startValue: int, destValue: int):
            return_pkg = {"pathToStart": None, "pathToDest": None, "path": None}
            if not root:
                return return_pkg
                
            lst_result = helper(root.left , startValue, destValue)
            rst_result = helper(root.right, startValue, destValue)
            
            if lst_result["path"]:
                return lst_result
            
            if rst_result["path"]:
                return rst_result
            
            if lst_result["pathToStart"] or rst_result["pathToStart"]:
                if lst_result["pathToStart"]:
                    return_pkg["pathToStart"] = lst_result["pathToStart"] 
                else:
                    return_pkg["pathToStart"] = rst_result["pathToStart"]   
                
            if lst_result["pathToDest"] or rst_result["pathToDest"]:
                if lst_result["pathToDest"]:
                    return_pkg["pathToDest"] = lst_result["pathToDest"] 
                else:
                    return_pkg["pathToDest"] = rst_result["pathToDest"]

            if root.val == startValue:
                return_pkg["pathToStart"] = [root]
            elif return_pkg["pathToStart"]:
                return_pkg["pathToStart"].append(root)
                
            if root.val == destValue:
                return_pkg["pathToDest"] = [root]
            elif return_pkg["pathToDest"]:
                return_pkg["pathToDest"].append(root)
            
            if return_pkg["pathToStart"] and return_pkg["pathToDest"]:
                path = "U" * (len(return_pkg["pathToStart"]) - 1)
                u = return_pkg["pathToDest"].pop()
                while return_pkg["pathToDest"]:
                    v = return_pkg["pathToDest"].pop()
                    path += "L" if u.left == v else "R"
                    u = v
                    
                return_pkg["pathToStart"] = None
                return_pkg["pathToDest"]  = None               
                return_pkg["path"] = path
                
            return return_pkg 
        
        return helper(root, startValue, destValue)["path"]