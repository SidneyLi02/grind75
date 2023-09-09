# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # def invertTree(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: TreeNode
    #     """
    #     # using postorder tree traversal, recursion
    #     # helpful link for refresher: https://cs-people.bu.edu/tvashwin/cs112_spring09/lab06_files/tree_example.png
    #     if not root:
    #         return root # base case: leaf
    #     else:
    #         self.invertTree(root.left) # recursive on left subtree
    #         self.invertTree(root.right) # recursive on right subtree
    #         root.left, root.right = root.right, root.left # swapping left with right subtree at parent level
    #         return root
        
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # iterative method using stack, more intuitive
        stack = [root]
        while stack:
            curr_node = stack.pop()
            if curr_node:
                curr_node.left, curr_node.right = curr_node.right, curr_node.left
                stack += curr_node.left, curr_node.right
        return root
        