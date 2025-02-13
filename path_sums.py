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
        if not root: return []

        def dfs(root, currSum, path):
            nonlocal paths
            left, right = [], []
            currSum += root.val
            path = path.copy()
            path.append(root.val)
            
            if self.isLeaf(root):
                if currSum == targetSum:
                    return paths.append(path)

            if root.left:
                dfs(root.left, currSum, path)
            
            if root.right:
                dfs(root.right, currSum, path)    

        paths = []
        dfs(root, 0, []) 
        return paths
