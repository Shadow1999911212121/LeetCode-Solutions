class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        results = []
        
        def backtrack(remain: int, combo: list, start: int):
            # Base Case: if the combination reaches the desired length
            if len(combo) == k:
                if remain == 0:
                    results.append(list(combo))
                return
            
            # Optimization: if the remaining sum is negative, stop exploring
            if remain < 0:
                return
            
            # Iterate through valid numbers from 'start' to 9
            for num in range(start, 10):
                combo.append(num)
                # Move to the next number (num + 1) to ensure uniqueness
                backtrack(remain - num, combo, num + 1)
                combo.pop() # Backtrack
                
        backtrack(n, [], 1)
        return results