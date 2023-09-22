# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def __init__(self):
        self.diameter = 0
        
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # return self.maxDepth(root.left) + self.maxDepth(root.right)
        self.maxDepth(root)
        return self.diameter
        
    def maxDepth(self, root):
        if root is None:
            return 0
        # Calculate max depth of left, right subtrees
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        # Calculate diameter
        if left + right > self.diameter:
            self.diameter = left + right
        return 1 + max(left, right)
