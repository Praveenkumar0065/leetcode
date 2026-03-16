class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums:
            return []
        
        # 1. Sorting
        nums.sort()

        # 2. Initializing and start
        ans = []
        for n in range(len(nums)-3):
            # Removing duplicate
            if n > 0 and nums[n] == nums[n-1]:
                continue
            
            # Min sum for the current index
            minSum = nums[n] + nums[n+1] + nums[n+2] + nums[n+3]
            if minSum > target:
                break
            
            # Max sum for the current index
            maxSum = nums[n] + nums[len(nums)-1] + nums[len(nums)-2] + nums[len(nums)-3]
            if maxSum < target:
                continue
            
            for m in range(n+1, len(nums)-2):
                if m > n+1 and nums[m] == nums[m-1]:
                    continue
                # Doing it again for max and min but including n 
                min_m = nums[n] + nums[m] + nums[m+1] + nums[m+2]
                if min_m > target:
                    break 
                max_m = nums[n] + nums[m] + nums[len(nums)-1] + nums[len(nums)-2]
                if max_m < target:
                    continue
                
                # Similar with 3sum
                l    = m + 1
                r    = len(nums) - 1
                need = target - nums[n] - nums[m]
                while l < r:
                    s = nums[l] + nums[r]
                    if s == need:
                        ans.append([nums[n], nums[m], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        
                        # Removing duplicate from the 2pointers 
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                        while l < r and nums[r] == nums[r+1]:
                            r -= 1
                    elif s < need:
                        l += 1
                    else:
                        r -= 1
        return ans