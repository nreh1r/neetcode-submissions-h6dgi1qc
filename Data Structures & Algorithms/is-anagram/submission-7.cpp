class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) {
            return false;
        }

        unordered_map<char, int> s_map;
        unordered_map<char, int> t_map;

        for (size_t i = 0; i < s.size(); i++) {
            if (s_map.find(s[i]) == s_map.end()) {
                s_map.insert({s[i], 1});
            } else {
                s_map[s[i]] += 1;
            }

            if (t_map.find(t[i]) == t_map.end()) {
                t_map.insert({t[i], 1});
            } else {
                t_map[t[i]] += 1;
            }
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
