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

function smallestFromLeaf(root: TreeNode | null): string {
    
    const reverse = (a: number[]) => {
        const copy = [...a]
        let i = 0;
        let j = copy.length - 1;
        while (i < j) {
            const temp = copy[i]
            copy[i] = copy[j];
            copy[j] = temp;
            i++;
            j--;
        }
        return copy;
    }
    
    const convert = (a: number[]) => {
        let s = "";
        for (let i = 0; i < a.length; i++) {
            s += String.fromCharCode(97 + a[i]);
        }
        return s;
    }
    
    let smallest = [26];
    
    const helper = (root: TreeNode | null, prefix: number[]) => {
        if (!root) {
            return;
        }
        const prefixCopy = [...prefix];
        prefixCopy.push(root.val);
        if (!root.left && !root.right) {
            const newPrefix = reverse(prefixCopy);
            for (let i = 0; i < newPrefix.length; i++) {
                if (newPrefix[i] > smallest[i]) {
                    return;
                } else if (newPrefix[i] < smallest[i]) {
                    break;
                }
                if (i == smallest.length) {
                    return;
                }
            }
            smallest = newPrefix;
        } else {
            helper(root.left, prefixCopy);
            helper(root.right, prefixCopy);
        }
    }
    
    helper(root, []);
    return convert(smallest);
};
