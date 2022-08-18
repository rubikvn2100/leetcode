# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        def analyzeTree(root: Optional[TreeNode]):
            return_pkg = {"qualifyNum": None, "sum": None, "numChildrent": None}
            if not root:
                return_pkg["sum"] = 0
                return_pkg["qualifyNum"] = 0
                return_pkg["numChildrent"] = 0
                return return_pkg
            
            return_pkg["sum"] = root.val
            return_pkg["qualifyNum"] = 1
            return_pkg["numChildrent"] = 1

            lst_pkg = analyzeTree(root.left )
            rst_pkg = analyzeTree(root.right)
            
            return_pkg["sum"]          += lst_pkg["sum"]          + rst_pkg["sum"]
            return_pkg["numChildrent"] += lst_pkg["numChildrent"] + rst_pkg["numChildrent"]
            
            return_pkg["qualifyNum"] = lst_pkg["qualifyNum"] + rst_pkg["qualifyNum"]
            if root.val == int(return_pkg["sum"] / return_pkg["numChildrent"]):
                return_pkg["qualifyNum"] += 1
                
            return return_pkg
        
        return analyzeTree(root)["qualifyNum"]
                
        