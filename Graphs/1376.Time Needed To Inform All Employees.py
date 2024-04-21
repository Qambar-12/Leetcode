class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        #directed acyclic graph question (no cycles here we just need to go from manager to employee)
        #building an adjacency list i.e each manager mapped to its subordinate employees    
        adj = collections.defaultdict(list)   ##Manager : [list of employees]
        for i in range(n):
            adj[manager[i]].append(i)
        #BFS level order Traversal
        #time to inform everyone must be the one maximum time of a node(employee)
        res = 0
        q = deque([(headID,0)])     #tuple pair ---> (id,time to reach node)  
        while q:
            id_ , time = q.popleft()
            res = max(res,time)
            for emp in adj[id_]:
                #time to reach manager and then add time it takes to tell manager to employee
                q.append((emp, time + informTime[id_]))
        return res    
