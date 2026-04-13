class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_map = {}
        t_map = {}

        for i in range(len(s)):
            s_char = s[i]
            t_char = t[i]

            if s_char in s_map:
                s_map[s_char] += 1
            else:
                s_map[s_char] = 1
            
            if t_char in t_map:
                t_map[t_char] += 1
            else:
                t_map[t_char] = 1
            
        if len(s_map) != len(t_map):
            return False
        
        for key, value in s_map.items():
            if key not in t_map:
                return False
            elif value != t_map[key]:
                return False
        
        return True