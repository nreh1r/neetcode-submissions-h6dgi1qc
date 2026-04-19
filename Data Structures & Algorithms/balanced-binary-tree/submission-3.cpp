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
    bool result = true;
    bool isBalanced(TreeNode* root) {
        dfs(root);

        return result;    
    }

    int dfs(TreeNode* root) {
        if (!root) {
            return 0;
        }

        int left = dfs(root->left);
        int right = dfs(root->right);

        if (abs(right - left) > 1) {
            result = false;
        }

        return 1 + max(left, right);
    }
};
