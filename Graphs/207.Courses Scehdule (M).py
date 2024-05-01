class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #for each course there can be some prerequisites which can be represented in a graph via outdegrees from a node
        #building an adjacency list (neighbouring or connected nodes) for each course
        if not len(prerequisites): return True
        adjList = {i:[] for i in range(numCourses)}
        for course,pre in prerequisites:
            adjList[course].append(pre)
        #DFS ---> checks for that a particular course can be completed without any cycle and then recursively runs for prerequisite courses
        #keeps track of all courses along current dfs path
        visitSet = set()
        def dfs(course):
            #i.e a cycle (infinite loop) detected in graph (Base case 1)
            if course in visitSet:
                return False
            #if a particular course has no prerequisite (Base case 2)
            if not adjList[course] :
                return True
            visitSet.add(course)
            #for each prereq course running the dfs recursively
            for pre in adjList[course]:
                if not dfs(pre) : return False
            #i.e we are successfully done with all prereq of courses 
            visitSet.remove(course)  
            adjList[course] = []  
            return True

        #finally need to call dfs but we need to loop through each of them manually in case they are disconnected
        for course in range(numCourses):
            if not dfs(course): return False
        return True    
                    
