# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isLeaf(self,root):
        if not root.left and not root.right:
            return True
        return False

    def getLeafNodes(self, root):
        # Will return the leaf nodes for given tree
        left, right = [],[]
        if self.isLeaf(root):
            return [root.val]
        
        if root.left:
            left = self.getLeafNodes(root.left)

        if root.right:
            right = self.getLeafNodes(root.right)
        
        return left + right 
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # Get the leaf nodes of both trees. 
        if not root1 or not root2: return True
        root1_leaf = self.getLeafNodes(root1)
        root2_leaf = self.getLeafNodes(root2)
        return root1_leaf == root2_leaf
