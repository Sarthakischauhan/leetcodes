# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sys

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, maxVal):

            if root is None: return
            nonlocal count
            if maxVal <= root.val:
                count += 1
                maxVal = root.val
            
            dfs(root.left, maxVal)
            dfs(root.right, maxVal) 
        
        count = 0
        # This neat trick is taken from dear old stack overflow
        minNumber = float('-inf')
    
        dfs(root, minNumber)
        return count
        
