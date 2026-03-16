class Solution:
    def maxArea(self, height: List[int]) -> int:
        ret = 0
        n = len(height)
        maxHeight = max(height)

        left = 0
        right = n - 1

        while (left != right):
            volume = (right - left) * min(height[left], height[right])
            ret = max(ret, volume)

            if (ret > maxHeight * (right - left)):
                return ret

            if height[right] < height[left]:
                right -= 1
            else:
                left += 1

        return ret