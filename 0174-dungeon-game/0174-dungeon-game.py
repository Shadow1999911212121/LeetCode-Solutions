from typing import List

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m = len(dungeon)
        n = len(dungeon[0])
        
        # Create a DP table to store the min health needed at each cell
        dp = [[0] * n for _ in range(m)]
        
        # Base case: The bottom-right cell
        # The knight needs at least 1 HP to survive. 
        # If the room has negative value (demons), he needs 1 - dungeon[m-1][n-1] HP.
        # If the room has positive value (orbs), he still needs at least 1 HP.
        dp[m-1][n-1] = max(1, 1 - dungeon[m-1][n-1])
        
        # Fill the last column (can only move down)
        for i in range(m - 2, -1, -1):
            dp[i][n-1] = max(1, dp[i+1][n-1] - dungeon[i][n-1])
            
        # Fill the last row (can only move right)
        for j in range(n - 2, -1, -1):
            dp[m-1][j] = max(1, dp[m-1][j+1] - dungeon[m-1][j])
            
        # Fill the rest of the grid
        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                # The knight chooses the path that requires less health
                min_health_on_exit = min(dp[i+1][j], dp[i][j+1])
                dp[i][j] = max(1, min_health_on_exit - dungeon[i][j])
                
        return dp[0][0]
