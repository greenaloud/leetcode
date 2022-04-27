class Solution(object):
    def search(self, nums, target):
        lt = 0
        rt = len(nums) - 1
        while lt <= rt:
            mid = lt + (rt - lt) // 2
            if nums[mid] < target:
                lt = mid + 1
            elif nums[mid] > target:
                rt = mid - 1
            else:
                return mid
        return -1
