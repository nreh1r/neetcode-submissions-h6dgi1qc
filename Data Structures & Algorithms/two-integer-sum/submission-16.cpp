class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> num_map;

        for (size_t i = 0; i < nums.size(); i++) {
            int value = nums[i];
            int diff = target - value;
            int index = i;

            if (num_map.find(diff) != num_map.end()) {
                return {num_map[diff], index};
            }

            num_map[value] = i;
        }

        return {};
    }
};
