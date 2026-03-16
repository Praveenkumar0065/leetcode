class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(index, current_combo, current_sum):
            if current_sum == target:
                res.append(list(current_combo))
                return
            if current_sum > target or index >= len(candidates):
                return
            current_combo.append(candidates[index])
            backtrack(index, current_combo, current_sum + candidates[index])
            current_combo.pop()
            backtrack(index + 1, current_combo, current_sum)

        backtrack(0, [], 0)
        return res
