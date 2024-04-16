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

function addOneRow(root: TreeNode | null, val: number, depth: number): TreeNode | null {
    const helper = (root: TreeNode | null, val: number, depth: number, dir: string) => {
        if (!root) {
            if (depth == 1) {
                return new TreeNode(val);
            } else {
                return null;
            }
        } else if (depth == 1) {
            let newRoot;
            if (dir === "left") {
                newRoot = new TreeNode(val, root, null);
            } else {
                newRoot = new TreeNode(val, null, root);
            }
            return newRoot;
        } else {
            const leftTree = helper(root.left, val, depth - 1, "left");
            const rightTree = helper(root.right, val, depth - 1, "right");
            return new TreeNode(root.val, leftTree, rightTree);
        }
    }
    
    return helper(root, val, depth, "left");
};
