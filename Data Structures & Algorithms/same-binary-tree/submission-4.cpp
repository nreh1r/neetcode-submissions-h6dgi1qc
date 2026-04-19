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
    bool isSameTree(TreeNode* p, TreeNode* q) {
        dfs(p, q);

        return result;
    }

    void dfs(TreeNode* t1, TreeNode* t2) {
        if (!t1 && !t2) {
            return;
        }

        if ((!t1 && t2) || (!t2 && t1) || (t1->val != t2->val)) {
            result = false;
            return;
        }

        dfs(t1->left, t2->left);
        dfs(t1->right, t2->right);
    }
};
