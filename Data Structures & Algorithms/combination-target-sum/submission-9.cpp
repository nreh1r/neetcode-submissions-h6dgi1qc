class Solution {
public:
    vector<vector<int>> res;
    vector<vector<int>> combinationSum(vector<int>& nums, int target) {
        vector<int> subset;
        dfs(0, subset, 0, target, nums);
        return res;
    }
    void dfs(int idx, vector<int> subset, int count, int target, vector<int>& nums) {
        if (count == target) {
            res.push_back(subset);
            return;
        } else if (idx >= nums.size() || count > target) {
            return;
        }

        subset.push_back(nums[idx]);
        dfs(idx, subset, count + nums[idx], target, nums);
        subset.pop_back();
        dfs(idx + 1, subset, count, target, nums);
    }
};
