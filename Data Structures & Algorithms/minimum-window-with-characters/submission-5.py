class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_map = {}
        # Map over t to get the counts needed
        for c in t:
            t_map[c] = t_map.get(c, 0) + 1
        
        # Set tracking variables
        need = len(t_map)
        have = 0
        l, r = 0, 0
        s_map = {}
        result = ""

        while l < len(s) and r < len(s):
            while l < len(s) and s[l] not in t_map:
                # This will only execute when trying to find a new solution
                l += 1
                r = l
            
            # Need to start incrementing r
            if r < len(s) and s[r] in t_map:
                s_map[s[r]] = s_map.get(s[r], 0) + 1

                # Check if this is another match
                if s_map[s[r]] == t_map[s[r]]:
                    have += 1
                
            # Check for full solution
            if have == need:
                res = s[l:r + 1]
                if result == "" or len(result) > len(res):
                    result = res
                s_map = {}
                have = 0
                l += 1
                r = l
            else:
                r += 1

        return result

