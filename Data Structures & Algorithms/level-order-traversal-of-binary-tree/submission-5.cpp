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
        queue<tuple<TreeNode*, int>> traversal_queue;
        vector<vector<int>> result;

        if (root) {
            traversal_queue.push({root, 0});
        }

        while (traversal_queue.size() > 0) {
            auto [node, level] = traversal_queue.front();
            traversal_queue.pop();

            if (result.size() <= level) {
                result.push_back(vector<int>());
            }

            result[level].push_back(node->val);

            if (node->left) {
                traversal_queue.push({node->left, level + 1});
            }

            if (node->right) {
                traversal_queue.push({node->right, level + 1});
            }
        }

        return result;
    }
};
