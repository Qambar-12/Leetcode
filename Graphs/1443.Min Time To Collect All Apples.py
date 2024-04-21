class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        #bidirectional arrows makes it a graph rather than a tree
        #each node can have max three neighbours and we make no distinction b/w parent and child actually b/c its a graph not a tree
        adj = {i:[] for i in range(n)}
        #making a list of neighbours:
        for par , child in edges:
            adj[par].append(child)
            adj[child].append(par)
        #DFS --> Recursive algorithm is used to check how much time it takes to collect apples from a subtree    
        #we are going to add 2 for sure if there is an apple at child spot wrt to curr parent node
        #condition for adding 2 (going down and back up) iff child itself has an apple or return value from subtree is > 0 i.e some descendent apples that are not immediate childs
        #a leaf node/vertex return zero b/c it has no left and right child so it take 0 sec to collect apples from both subtrees
        #O(n) ---> time complexity b/c we only have to traverse all vertices of graphs
        #we might get stcuk into infinite loop if we go from par to child and from child back to parent
        #so only parameter we need to pass with curr is par 
        def dfs(curr,par):
            time = 0
            for child in adj[curr]:
                #if neighbour of vertex in list is parent up we need to skip it to prevent infinite loop
                #e.g {0:[1,2],1:[0,4,5],......}
                #so when it is called recursively and goes to child 1 its neighbour also include parent '0'
                if child == par:
                    continue
                childTime = dfs(child,curr)
                #i.e if return value is positive i.e subtree has apples to collect or child itself has apple
                if childTime or hasApple[child]:
                    time += 2 + childTime    
            return time
        return dfs(0,-1)    