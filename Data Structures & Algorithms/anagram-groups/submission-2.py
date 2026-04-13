class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        # Need to loop through each string
        for val in strs:
            # Need to count the number of letters
            char_arr = [0] * 26
            for char in val:
                char_arr[ord(char) - ord("a")] += 1
            key = tuple(char_arr)
            if key in groups:
                groups[key].append(val)
            else:
                groups[key] = [val]
        
        return groups.values()