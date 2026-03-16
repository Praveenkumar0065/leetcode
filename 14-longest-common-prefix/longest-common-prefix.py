class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""            
        strs.sort()
        first, last = strs[0], strs[-1]
        res = ""        
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                break
            res += first[i]
            
        return res
