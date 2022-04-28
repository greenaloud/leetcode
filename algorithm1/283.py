class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        lt = 0
        rt = 1
        while rt < n:
            while rt < n and nums[rt] == 0:
                rt += 1
            while lt < rt and nums[lt]:
                lt += 1
            if n > rt > lt:
                nums[lt], nums[rt] = nums[rt], nums[lt]
            lt, rt = lt + 1, rt + 1
