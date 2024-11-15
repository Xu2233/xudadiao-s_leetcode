class Solution(object):
    def countGoodNodes(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        edges[i] = [ai,bi]表示ab存在一条边
        如果一个节点的所有子节点为根的子树包含的节点数相
        """
        graph = [[]for edge in range(len(edges))]
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        print(graph)

        def dfs(graph,parent):
            count = 0
            for neighboor in graph[node]:
                if neighboor != parent:
                    count += dfs(neighboor,node)
            return count
        
        good_nodes = 0




c =    Solution()
edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]]
print(c.countGoodNodes(edges))
        