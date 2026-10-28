class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [set() for _ in range(n)]
        dp[0].add(grid[0][0])
        for j in range(1, n):
            for prev_xor in dp[j - 1]:
                dp[j].add(prev_xor ^ grid[0][j])
        for i in range(1, m):
            new_dp = [set() for _ in range(n)]
            for j in range(n):
                for prev_xor in dp[j]:
                    new_dp[j].add(prev_xor ^ grid[i][j])
                if j > 0:
                    for prev_xor in new_dp[j - 1]:
                        new_dp[j].add(prev_xor ^ grid[i][j])
            dp = new_dp
            
        return min(dp[n - 1])

        