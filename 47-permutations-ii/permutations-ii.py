from collections import Counter
from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        results = []
        def backtrack(comb, counter):
            if len(comb) == len(nums):
                results.append(list(comb))
                return            
            for num in counter:
                if counter[num] > 0:
                    comb.append(num)
                    counter[num] -= 1
                    backtrack(comb, counter)
                    counter[num] += 1
                    comb.pop()
        backtrack([], Counter(nums))
        return results