class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_map = defaultdict(int)
        
        # Map s1 to get the counts
        for s in s1:
            s1_map[s] += 1
        print(s1_map)
        
        # Use a sliding window over s2
        for l in range(len(s2)):
            # Check is the current character is in s1
            # print(s2[l], s1_map, s2[l] in s1_map)
            if s2[l] in s1_map:
                # Start the sliding window
                s2_map = defaultdict(int)
                r = l
                while r < len(s2) and s2[r] in s1_map and s2_map[s2[r]] < s1_map[s2[r]]:
                    print(s2_map)
                    s2_map[s2[r]] += 1
                    r += 1
                    print(s2_map)
                
                if s1_map == s2_map:
                    return True
                print("done iteration")
        return False
            
