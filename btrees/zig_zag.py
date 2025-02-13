# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isLeaf(self, root):
        return not root.left and not root.right

    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def dfs(root, direction, count):
            if root is None:
                return count - 1  

            if direction == "left":
                left = dfs(root.right, "right", count + 1)
                right = dfs(root.left, "left", 1) if root.left else 0

            if direction == "right":
                left = dfs(root.left, "left", count + 1)
                right = dfs(root.right, "right", 1) if root.right else 0

            
            return max(left, right)
        

        maxCount = max(dfs(root.right, "right", 1), dfs(root.left, "left", 1))
        return maxCount


