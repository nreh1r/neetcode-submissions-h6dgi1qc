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
    void dfs(TreeNode* root) {
        if (!root) {
            return;
        }

        int leftMax = getMax(root->left);
        int rightMax = getMax(root->right);
        pathSum = max(pathSum, root->val + leftMax + rightMax);

        dfs(root->left);
        dfs(root->right);
    }

    int getMax(TreeNode* root) {
        if (!root) {
            return 0;
        }

        int leftPath = getMax(root->left);
        int rightPath = getMax(root->right);
        int val = root->val + max(leftPath, rightPath);

        return max(0, val);
    }
};
