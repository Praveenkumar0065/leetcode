class Solution:
    def searchInsert(self, n: List[int], t: int) -> int:
        l,r=0,len(n)-1
        while l<=r:
            m=(r+l)//2
            if n[m] ==t:
                return m
            elif n[m]<t:
                l=m+1
            else:
                r=m-1
        return l