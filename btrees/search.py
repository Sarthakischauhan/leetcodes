from traversals import TreeNode

T = TreeNode()

# Only applies for Binary Search Trees (Specifies a specific need)

def searchKey(root, key):
    # Searches for a key in a binary tree using recursive approach
    if root is None or root.val == key:
        return root 
    
    if root.val < key:
        return searchKey(root.right, key)
    else:
        return searchKey(root.left, key)


def minimumKey(root):
    if root.left != None:
        return minimumKey(root.left)
    else:
        return root.val

def maximumKey(root):
    if root.right != None:
        return maximumKey(root.right)
    else:
        return root.val

def treeSuccessor(node):
    if node.right:
        return minimumKey(node.right)
    # Later instruction unclear for now.


root = TreeNode(15)
root.left = TreeNode(6)
root.right = TreeNode(18)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.left = TreeNode(17)
root.right.right = TreeNode(20)

x = searchKey(root, 15)
min = minimumKey(root)
max = maximumKey(root)
print(f"Minimum key is : {min}")
print(f"Maximum key is : {max}")
