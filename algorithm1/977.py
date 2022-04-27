class Solution(object):
    def sortedSquares(self, nums):
        lt = 0
        rt = len(nums) - 1
        idx = rt
        ans = [0] * len(nums)
        while lt <= rt:
            if abs(nums[lt]) > abs(nums[rt]):
                ans[idx] = nums[lt] ** 2
                lt += 1
            else:
                ans[idx] = nums[rt] ** 2
                rt -= 1
            idx -= 1

        return ans
