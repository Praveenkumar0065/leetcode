from collections import Counter
from typing import List

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        row_counts = Counter(tuple(row) for row in grid)
        pair_count = 0        
        for col in zip(*grid):
            pair_count += row_counts[col]            
        return pair_count
