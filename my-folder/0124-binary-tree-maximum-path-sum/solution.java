/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    int maxValue;

    public int maxPathSum(TreeNode root) {
        if (root == null) {return 0;}
        maxValue = Integer.MIN_VALUE;
        maxPathDown(root);
        return maxValue;
    }

    public int maxPathDown(TreeNode root) {
        if (root == null) {
            return 0;
        } 
        int left = Math.max(0, maxPathDown(root.left));
        int right = Math.max(0, maxPathDown(root.right));
        maxValue = Math.max(maxValue, root.val + left + right);
        return Math.max(left, right) + root.val;
    }
}
