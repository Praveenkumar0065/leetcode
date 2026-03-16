class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        # d1[r][c] is the prefix sum of diagonal from top-left to bottom-right
        # d2[r][c] is the prefix sum of diagonal from top-right to bottom-left
        d1 = [[0] * (n + 2) for _ in range(m + 2)]
        d2 = [[0] * (n + 2) for _ in range(m + 2)]
        
        for r in range(m):
            for c in range(n):
                d1[r+1][c+1] = grid[r][c] + d1[r][c]
                d2[r+1][c+1] = grid[r][c] + d2[r][c+2]
        
        sums = set()
        for r in range(m):
            for c in range(n):
                sums.add(grid[r][c]) # Area 0 rhombus
                
                for k in range(1, min(m, n)):
                    # Check if rhombus corners are within bounds
                    # Corners: Top (r-k, c), Bottom (r+k, c), Left (r, c-k), Right (r, c+k)
                    if r - k < 0 or r + k >= m or c - k < 0 or c + k >= n:
                        break
                    
                    # Sum the four edges using diagonal prefix sums:
                    # Edge 1 (Top to Right): Diagonal 1
                    s1 = d1[r+1][c+k+1] - d1[r-k][c]
                    # Edge 2 (Top to Left): Diagonal 2
                    s2 = d2[r+1][c-k+1] - d2[r-k][c+2]
                    # Edge 3 (Left to Bottom): Diagonal 1
                    s3 = d1[r+k+1][c+1] - d1[r][c-k]
                    # Edge 4 (Right to Bottom): Diagonal 2
                    s4 = d2[r+k+1][c+1] - d2[r][c+k+2]
                    
                    # Corners are added twice in s1+s2+s3+s4, so subtract them once
                    total = s1 + s2 + s3 + s4 - (grid[r-k][c] + grid[r+k][c] + grid[r][c-k] + grid[r][c+k])
                    sums.add(total)
                    
        return sorted(list(sums), reverse=True)[:3]
