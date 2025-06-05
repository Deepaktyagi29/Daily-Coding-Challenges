from collections import defaultdict

class Solution:
    def countPaths(self, edges, V, src, dest):
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)

        def dfs(node):
            if node == dest:
                return 1
            if dp[node] != -1:
                return dp[node]
            total = 0
            for nei in graph[node]:
                total += dfs(nei)
            dp[node] = total
            return total

        dp = [-1] * V
        return dfs(src)

# Example usage:
if __name__ == "__main__":
    V = 5
    edges = [[0, 1], [0, 2], [1, 3], [2, 3], [3, 4]]
    src = 0
    dest = 4
    sol = Solution()
    print(sol.countPaths(edges, V, src, dest))
