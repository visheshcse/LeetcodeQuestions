//https://leetcode.com/problems/maximum-depth-of-binary-tree/

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
    public int findMaxDepth(TreeNode node){
        if(node == null){
            return 0;
        }
        int ls = 1 + findMaxDepth(node.left);
        int rs = 1 + findMaxDepth(node.right);
        return ls > rs ? ls : rs;
    }
    public int maxDepth(TreeNode root) {
        return findMaxDepth(root);
    }
}