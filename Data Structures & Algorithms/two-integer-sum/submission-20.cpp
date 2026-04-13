class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> num_map;

        for (int i = 0; i < nums.size(); i++) {
            int value = nums[i];
            int diff = target - value;
            auto it = num_map.find(diff);
            if (it != num_map.end()) {
                return {it->second, i};
            }

            num_map[value] = i;
        }

        return {};
    }
};
