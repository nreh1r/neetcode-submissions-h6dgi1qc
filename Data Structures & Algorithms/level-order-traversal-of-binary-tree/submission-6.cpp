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
    vector<vector<int>> levelOrder(TreeNode* root) {
        queue<tuple<TreeNode*, int>> t_queue;
        vector<vector<int>> res;

        if (root) {
            t_queue.push({root, 0});
        }

        while (t_queue.size() > 0) {
            auto [node, level] = t_queue.front();
            t_queue.pop();

            if (res.size() <= level) {
                res.push_back(vector<int>());
            }

            res[level].push_back(node->val);

            if (node->left) {
                t_queue.push({node->left, level + 1});
            }

            if (node->right) {
                t_queue.push({node->right, level + 1});
            }
        }

        return res;
    }
};
