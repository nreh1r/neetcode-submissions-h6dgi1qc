/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    int pathSum = 0;
    int maxPathSum(TreeNode* root) {
        pathSum = root->val;
        dfs(root);
        return pathSum;
    }
    int dfs(TreeNode* root) {
        if (!root) {
            return 0;
        }

        int leftPath = dfs(root->left);
        int rightPath = dfs(root->right);
        int leftMax = max(0, leftPath);
        int rightMax = max(0, rightPath);
        pathSum = max(pathSum, root->val + leftMax + rightMax);

        return root->val + max(leftMax, rightMax);
    }
};
