# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        current_node = root
        p_ancestors = set()
        p_ancestors.add(p)
        while current_node.val != p.val:
            p_ancestors.add(current_node)
            if current_node.val > p.val:
                current_node = current_node.left
            else:
                current_node = current_node.right
        current_node = root
        common_ancestor = root
        while current_node in p_ancestors:
            common_ancestor = current_node
            if current_node.val > q.val:
                current_node = current_node.left
            elif current_node.val < q.val:
                current_node = current_node.right
            else:
                break
        return common_ancestor
