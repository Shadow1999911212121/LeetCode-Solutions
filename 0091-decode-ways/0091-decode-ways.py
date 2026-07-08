class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        
        n = len(s)
        # dp[i] represents the number of ways to decode the substring s[0:i]
        dp = [0] * (n + 1)
        
        # Base cases
        dp[0] = 1 # Empty string has one way to be decoded
        dp[1] = 1 # First character is valid (checked above)
        
        for i in range(2, n + 1):
            # Check single digit decoding
            one_digit = int(s[i-1])
            if one_digit != 0:
                dp[i] += dp[i-1]
            
            # Check two digit decoding
            two_digits = int(s[i-2:i])
            if 10 <= two_digits <= 26:
                dp[i] += dp[i-2]
                
        return dp[n]
