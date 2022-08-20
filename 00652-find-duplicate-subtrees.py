# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    class TreeData:
        def __init__(self, numNode = 0, preOrder = [], numOccurrence = 0, sampleTree = None):
            self.numNode       = numNode
            self.preOrder      = preOrder
            self.numOccurrence = numOccurrence
            self.sampleTree    = sampleTree
            
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        MAX_INT = 10**9
        uniqueTreeDataList = []
        def analyzeTree(root: Optional[TreeNode]):
            if not root: 
                return self.TreeData()

            lst_TreeData = analyzeTree(root.left)
            rst_TreeData = analyzeTree(root.right)
            currentNumNode  = 1 + lst_TreeData.numNode + rst_TreeData.numNode 
            currentPreOrder = [root.val]
            if root.left or root.right:
                currentPreOrder += lst_TreeData.preOrder if root.left  else [MAX_INT]
                currentPreOrder += rst_TreeData.preOrder if root.right else [MAX_INT]
            
            for treeData in uniqueTreeDataList:
                if currentNumNode == treeData.numNode and currentPreOrder == treeData.preOrder:
                    treeData.numOccurrence += 1
                    return treeData
            
            current_TreeData = self.TreeData(currentNumNode, currentPreOrder, 1, root)
            uniqueTreeDataList.append(current_TreeData)
            return current_TreeData
        
        analyzeTree(root)
        duplicateTreeRoot = []
        for treeData in uniqueTreeDataList:
            if treeData.numOccurrence > 1:
                duplicateTreeRoot.append(treeData.sampleTree)
                
        return duplicateTreeRoot