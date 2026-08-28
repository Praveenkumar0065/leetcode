from collections import Counter
from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        results = []
        def backtrack(comb, counter):
            # If the current combination is done
            if len(comb) == len(nums):
                results.append(list(comb))
                return
            
            for num in counter:
                if counter[num] > 0:
                    # Choose the number
                    comb.append(num)
                    counter[num] -= 1
                    
                    # Continue down the recursion tree
                    backtrack(comb, counter)
                    
                    # Revert the choice (backtrack)
                    counter[num] += 1
                    comb.pop()
                    
        backtrack([], Counter(nums))
        return results
