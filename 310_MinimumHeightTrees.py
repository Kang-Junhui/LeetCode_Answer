class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        
        if n<=1:
            return [0]
        
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        leaf = []
        
        for i in range(n+1):
            if len(graph[i])==1:
                leaf.append(i)
        
        while n>2:
            n -= len(leaf)
            new = []
            for i in leaf:
                nei = graph[i].pop()
                graph[nei].remove(i)
                
                if len(graph[nei])==1:
                    new.append(nei)
            
            leaf = new
        
        return leaf
