class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) {
            return false;
        }

        unordered_map<char, int> s_map;
        unordered_map<char, int> t_map;

        for (size_t i = 0; i < s.size(); i++) {
            s_map[s[i]]++;
            t_map[t[i]]++;
        }

        for (auto it = s_map.begin(); it != s_map.end(); it++) {
            if (t_map.find(it->first) == t_map.end()) {
                return false;
            }

            if (t_map[it->first] != it->second) {
                return false;
            }
        }

        return true;
    }
};
