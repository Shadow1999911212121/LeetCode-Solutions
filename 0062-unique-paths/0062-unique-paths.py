class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Create a 2D array (dp table) initialized with 1s
        # dp[i][j] will store the number of unique paths to reach cell (i, j)
        dp = [[1 for _ in range(n)] for _ in range(m)]
        
        # Fill the table
        # We start from (1, 1) because the first row and first column 
        # are always 1 (only one way to move straight down or straight right)
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        # The result is in the bottom-right cell
        return dp[m-1][n-1]
