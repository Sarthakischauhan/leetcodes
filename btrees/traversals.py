#! usr/bin/python3

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Traversal:
    def __init__(self,root, method):
        self.root = root
        self.method = method

    def inorder_iterative(self):
        stack = []
        res = [] 
        curr = self.root
        while curr is not None or len(stack) > 0:
            while curr is not None:
                stack.append(curr)
                curr = curr.left 
            curr = stack.pop()
            res.append(curr.val)
    
            curr = curr.right
        return res 
    
    def preorder_iterative(self):
        
        stack = [] 
        res = []
        curr = self.root

        while curr is not None or len(stack) > 0:
            while curr is not None:
                # Traverse in left tree now
                res.append(curr.val)
                stack.append(curr.right)
                curr = curr.left
            # Traverse in right tree now
            curr = stack.pop()
            if (curr != None):
                res.append(curr.val) 
                stack.append(curr.right)
                curr = curr.left

        return res
    
    def postorder_iterative(self):
        curr = self.root
        stack = []
        res = []

        # Still working on it.
    
    def levelorder_iterative(self):
        curr = self.root
        res = []
        stack = [curr]
        while len(stack) > 0:
            curr = stack.pop(0)
            res.append(curr.val)
            if (curr.left):
                stack.append(curr.left)
            if (curr.right):
                stack.append(curr.right)
        return res

method = "ITERATIVE"
# Sample data for traversals 
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

t = Traversal(root,method)
print(t.inorder_iterative())
print(t.preorder_iterative())
print(t.levelorder_iterative())
