# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isLeaf(self, root):
        return not root.left and not root.right

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: return 0

        def dfs(root, currSum):
            if not root: return 0 
            currSum += root.val
            count = 0 
            if currSum == targetSum:
                count += 1
              
            if root.left:
                count += dfs(root.left,currSum)
            
            if root.right:
                count += dfs(root.right, currSum)    
            
            return count

        def traverse(root):
            if root is None: return 0

            return dfs(root, 0) + traverse(root.right) + traverse(root.left)

        
        return traverse(root)
