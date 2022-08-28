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
import java.util.HashMap;

class Stats {
    int leftHeight;
    int rightHeight;
    int diameter;
    
    public Stats(int leftHeight, int rightHeight) {
        this.leftHeight = leftHeight;
        this.rightHeight = rightHeight;
        this.diameter = leftHeight + rightHeight;
    }
}

class Solution {
    
    int diameter = 0;
    
    Stats emptyStats = new Stats(0, 0);
    
    public int diameterOfBinaryTree(TreeNode root) {
        if (root == null) {
            return 0;
        } else {
            mapStats(root);
        }
        return diameter;
    }
    
    public Stats mapStats(TreeNode root) {
        if (root == null) {
            return emptyStats;
        } else {
            Stats leftStats = mapStats(root.left);
            Stats rightStats = mapStats(root.right);
            int leftHeight = 
                leftStats.leftHeight > leftStats.rightHeight
                ? leftStats.leftHeight
                : leftStats.rightHeight;
            int rightHeight = 
                rightStats.leftHeight > rightStats.rightHeight
                ? rightStats.leftHeight
                : rightStats.rightHeight;
            if (leftHeight + rightHeight > this.diameter) {
                this.diameter = leftHeight + rightHeight;
            }
            Stats ans = new Stats(leftHeight + 1, rightHeight + 1);
            return ans;
        }
    } 
}
