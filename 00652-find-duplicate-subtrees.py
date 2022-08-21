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
        uniqueTreeDataDict = {}
        uniqueNumNodeSet = set()
        def analyzeTree(root: Optional[TreeNode]):
            if not root: 
                return self.TreeData()

            lst_TreeData = analyzeTree(root.left)
            rst_TreeData = analyzeTree(root.right)
            currentNumNode  = 1 + lst_TreeData.numNode + rst_TreeData.numNode 
            currentPreOrder = '*' + str(root.val)
            if root.left or root.right:
                currentPreOrder += lst_TreeData.preOrder if root.left  else '*'
                currentPreOrder += rst_TreeData.preOrder if root.right else '*'
  
            if currentNumNode in uniqueNumNodeSet and currentPreOrder in uniqueTreeDataDict:
                uniqueTreeDataDict[currentPreOrder].numOccurrence += 1
                return uniqueTreeDataDict[currentPreOrder]             
            
            current_TreeData = self.TreeData(currentNumNode, currentPreOrder, 1, root)
            uniqueTreeDataDict[currentPreOrder] = current_TreeData
            uniqueNumNodeSet.add(current_TreeData.numNode)
            return current_TreeData
        
        analyzeTree(root)
        duplicateTreeRoot = []
        for treeData in uniqueTreeDataDict.values():
            if treeData.numOccurrence > 1:
                duplicateTreeRoot.append(treeData.sampleTree)
                
        return duplicateTreeRoot