/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

function sumNumbers(root: TreeNode | null): number {
    const helper = (root: TreeNode | null, prev: number) => {
        if (!root) {
            return 0;
        } else if (!root.left && !root.right) {
            return prev * 10 + root.val;
        } else {
            const left = helper(root.left, prev * 10 + root.val)
            const right = helper(root.right, prev * 10 + root.val);
            return left + right;
        }
    }
    return helper(root, 0);
};
