class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_map = {}
        for c in t:
            t_map[c] = t_map.get(c, 0) + 1
        
        have, need = 0, len(t_map)
        result = ""
        l = 0
        s_map = {}
        for r in range(len(s)):
            c = s[r]

            s_map[c] = s_map.get(c, 0) + 1

            if c in t_map and s_map[c] == t_map[c]:
                have += 1
            
            while have == need:
                # Manage new solution
                if result == "" or len(result) > r - l + 1:
                    result = s[l:r + 1]
                
                # Need to move the left pointer
                s_map[s[l]] -= 1
                if s[l] in t_map and s_map[s[l]] < t_map[s[l]]:
                    have -= 1
                l += 1
        
        return result

