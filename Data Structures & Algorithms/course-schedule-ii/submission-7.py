class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            adj_list[crs].append(pre)
        
        visiting, visited = set(), set()
        course_list = []

        def dfs(course):
            if course in visiting:
                return False
            
            if course in visited:
                return True
            
            visiting.add(course)

            for pre in adj_list[course]:
                if not dfs(pre):
                    return False
            
            visiting.remove(course)
            visited.add(course)
            course_list.append(course)

            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return []
        
        return course_list