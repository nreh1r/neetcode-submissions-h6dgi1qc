class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            adj_list[crs].append(pre)
        
        visiting = set()

        def dfs(course):
            if course in visiting:
                return False
            
            if adj_list[course] == []:
                return True
            
            visiting.add(course)

            for pre in adj_list[course]:
                if not dfs(pre):
                    return False
                
            visiting.remove(course)
            adj_list[course] = []

            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        
        return True