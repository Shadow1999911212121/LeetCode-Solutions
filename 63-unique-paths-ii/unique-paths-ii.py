from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        # If the starting point or end point is an obstacle, no path is possible
        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
            return 0
            
        # Initialize a DP table
        dp = [[0 for _ in range(n)] for _ in range(m)]
        
        # Starting point
        dp[0][0] = 1
        
        # Fill the DP table
        for i in range(m):
            for j in range(n):
                # If current cell is an obstacle, paths to here = 0
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    # Add paths from the top
                    if i > 0:
                        dp[i][j] += dp[i-1][j]
                    # Add paths from the left
                    if j > 0:
                        dp[i][j] += dp[i][j-1]
                        
        return dp[m-1][n-1]
