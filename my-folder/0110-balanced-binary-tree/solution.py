# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.getHeight(root) != -1
    
    def getHeight(self, root):
        if root == None:
            return 0
        else:
            leftHeight = self.getHeight(root.left)
            rightHeight = self.getHeight(root.right)
            if abs(leftHeight - rightHeight) > 1 or leftHeight == -1 or rightHeight == -1:
                return -1
            else:
                height = max(leftHeight, rightHeight) + 1
                return height
